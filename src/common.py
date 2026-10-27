"""Shared helpers: loading, the target, the split, the baseline, the conversion back to index points,
the metrics and the scorecard. Every notebook starts with the same setup cell (see any notebook).

Why everything funnels through here: the brief scores all models on identical test dates, with the
same one-day horizon, in index points, against the last-observed-value baseline. One shared file
makes that true by construction.
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd

from src import config


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_prices() -> pd.DataFrame:
    """The committed CSV, indexed by date, sorted, with a log_return column added."""
    df = pd.read_csv(repo_root() / config.DATA_FILE, parse_dates=["Date"], index_col="Date")
    df = df.sort_index()
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    return df


def target_series(df: pd.DataFrame) -> pd.Series:
    """The series the models work on, with the first undefined value dropped."""
    return df[config.TARGET].dropna()


def split(series: pd.Series):
    """Train / validation / test in time order, using the dates in config."""
    train = series.loc[: config.TRAIN_END]
    val = series.loc[config.TRAIN_END:config.VAL_END].iloc[1:]   # exclude the boundary day already in train
    test = series.loc[config.VAL_END:].iloc[1:]
    return train, val, test


# ----------------------------------------------------------------- back to index points

def to_price(pred: pd.Series, df: pd.DataFrame) -> pd.Series:
    """Convert a forecast of the target into a forecast of the closing value, in index points.

    log_return: predicted close_t = close_{t-1} * exp(predicted return_t)
    close:      already a price, returned unchanged
    Uses only the previous day's actual close, which is known when the forecast is made.
    """
    pred = pd.Series(pred).astype(float)
    if config.TARGET == "log_return":
        prev_close = df["Close"].shift(1).reindex(pred.index)
        return prev_close * np.exp(pred)
    return pred


def actual_price(index, df: pd.DataFrame) -> pd.Series:
    return df["Close"].reindex(index)


def last_value_baseline(index, df: pd.DataFrame) -> pd.Series:
    """The brief's baseline: tomorrow's close = today's close (a random walk forecast)."""
    return df["Close"].shift(1).reindex(index)


# ----------------------------------------------------------------- metrics (in whatever units you pass)

def mae(y_true, y_pred) -> float:
    y_true, y_pred = _align(y_true, y_pred)
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true, y_pred) -> float:
    y_true, y_pred = _align(y_true, y_pred)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def _align(y_true, y_pred):
    y_true = pd.Series(y_true).astype(float)
    y_pred = pd.Series(y_pred, index=getattr(y_pred, "index", y_true.index)).astype(float)
    both = pd.concat([y_true, y_pred], axis=1, join="inner").dropna()
    return both.iloc[:, 0].to_numpy(), both.iloc[:, 1].to_numpy()


# ----------------------------------------------------------------- results shared with part 3

class Stopwatch:
    """with common.Stopwatch() as sw: model.fit(...)   ->   sw.seconds  (computational cost for the report)"""
    def __enter__(self):
        self.start = time.perf_counter(); return self
    def __exit__(self, *exc):
        self.seconds = time.perf_counter() - self.start


def save_predictions(name: str, df: pd.DataFrame, pred_target: pd.Series, settings: dict | None = None, train_seconds: float | None = None) -> Path:
    """Every model calls this once, on the test set. Stores index-point predictions next to the actual
    close, plus a small JSON with the settings and training time, for part 3's scorecard."""
    pred_target = pd.Series(pred_target).astype(float)
    pred_price = to_price(pred_target, df)
    out = repo_root() / "results" / f"{name}_predictions.csv"
    pd.DataFrame({
        "actual_close": actual_price(pred_target.index, df),
        "predicted_close": pred_price,
        "actual_target": df[config.TARGET].reindex(pred_target.index),
        "predicted_target": pred_target,
    }).to_csv(out)
    meta = {"model": name, "target": config.TARGET, "window": config.WINDOW, "train_end": config.TRAIN_END, "val_end": config.VAL_END,
            "n_test": int(pred_target.notna().sum()), "train_seconds": train_seconds, "settings": settings or {}}
    (repo_root() / "results" / f"{name}_meta.json").write_text(json.dumps(meta, indent=2, default=str))
    return out


def scorecard() -> pd.DataFrame:
    """One table, in index points, for every results/<model>_predictions.csv found."""
    rows = []
    for f in sorted((repo_root() / "results").glob("*_predictions.csv")):
        p = pd.read_csv(f, parse_dates=[0], index_col=0)
        name = f.stem.replace("_predictions", "")
        meta_file = f.with_name(f"{name}_meta.json")
        meta = json.loads(meta_file.read_text()) if meta_file.exists() else {}
        rows.append({"model": name,
                     "MAE (index points)": mae(p["actual_close"], p["predicted_close"]),
                     "RMSE (index points)": rmse(p["actual_close"], p["predicted_close"]),
                     "n_test": int(p["predicted_close"].notna().sum()),
                     "first test date": p.index.min().date(), "last test date": p.index.max().date(),
                     "train seconds": meta.get("train_seconds")})
    return pd.DataFrame(rows).set_index("model").sort_values("RMSE (index points)")
