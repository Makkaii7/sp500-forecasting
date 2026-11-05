"""Write the three sets (train, validation, test) as CSV files, for anyone who wants to open and check them.

They are made from data/sp500_daily.csv with the dates in src/config.py, exactly as the setup cell of
every notebook does it. The notebooks keep using the setup cell (train, val, test); these files are a copy
for inspection. If the dates in src/config.py ever change, run this again:  python data/make_splits.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import common, config  # noqa: E402

df = common.load_prices()
y = common.target_series(df)
train, val, test = common.split(y)
out = Path(__file__).resolve().parent / "splits"
out.mkdir(exist_ok=True)
for name, part in [("train", train), ("validation", val), ("test", test)]:
    table = df.loc[part.index, ["Close", "log_return"]]
    table.to_csv(out / f"{name}.csv")
    print(f"{name:11s} {part.index.min().date()} to {part.index.max().date()}  {len(part):5d} days  -> data/splits/{name}.csv")
print(f"settings used: TRAIN_START={config.TRAIN_START}  TRAIN_END={config.TRAIN_END}  VAL_END={config.VAL_END}")
