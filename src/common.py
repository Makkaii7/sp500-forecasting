"""Shared helpers: loading, the target, the split, the baseline and the metrics.

Every notebook starts with:

    import sys, pathlib
    root = next(p for p in [pathlib.Path.cwd(), *pathlib.Path.cwd().parents] if (p / "src" / "config.py").exists())
    sys.path.insert(0, str(root))
    from src import config, common

so that the same notebook works in Colab and in Cursor.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from src import config


def repo_root() -> Path:
    here = Path(__file__).resolve()
    return here.parent.parent


def load_prices() -> pd.DataFrame:
    """The committed CSV, indexed by date, sorted, with a log_return column added."""
    df = pd.read_csv(repo_root() / config.DATA_FILE, parse_dates=["Date"], index_col="Date")
    df = df.sort_index()
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    return df


def target_series(df: pd.DataFrame) -> pd.Series:
    """The series the models forecast, with the first undefined value dropped."""
    return df[config.TARGET].dropna()


def split(series: pd.Series):
    """Train / validation / test in time order, using the dates in config."""
    train = series.loc[: config.TRAIN_END]
    val = series.loc[config.TRAIN_END:config.VAL_END].iloc[1:]   # exclude the boundary day already in train
    test = series.loc[config.VAL_END:].iloc[1:]
    return train, val, test


def naive_forecast(series: pd.Series) -> pd.Series:
    """Random walk baseline for a price level: tomorrow = today."""
    return series.shift(1)


def zero_forecast(series: pd.Series) -> pd.Series:
    """Random walk baseline for a return: expected change = 0."""
    return pd.Series(0.0, index=series.index)


def mean_forecast(series: pd.Series, train_mean: float) -> pd.Series:
    """Random walk with drift for a return: predict the training-set average return."""
    return pd.Series(train_mean, index=series.index)


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


def save_predictions(name: str, y_true: pd.Series, y_pred: pd.Series) -> Path:
    """Every model writes its test-set predictions here, so part 3 can compare them."""
    out = repo_root() / "results" / f"{name}_predictions.csv"
    pd.DataFrame({"actual": y_true, "predicted": pd.Series(y_pred, index=y_true.index)}).to_csv(out)
    return out


def scorecard() -> pd.DataFrame:
    """One table with MAE and RMSE for every results/<model>_predictions.csv found."""
    rows = []
    for f in sorted((repo_root() / "results").glob("*_predictions.csv")):
        p = pd.read_csv(f, parse_dates=[0], index_col=0)
        rows.append({"model": f.stem.replace("_predictions", ""), "MAE": mae(p["actual"], p["predicted"]), "RMSE": rmse(p["actual"], p["predicted"]), "n_test": len(p)})
    return pd.DataFrame(rows).set_index("model").sort_values("RMSE")
