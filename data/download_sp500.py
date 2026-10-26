"""Download the S&P 500 daily series once and save it as data/sp500_daily.csv.

Run from the repository root:  python data/download_sp500.py
"""
from pathlib import Path
import pandas as pd
import yfinance as yf

START = "2010-01-01"   # change only by group decision, then commit the new CSV
TICKER = "^GSPC"

out = Path(__file__).resolve().parent / "sp500_daily.csv"
data = yf.download(TICKER, start=START, auto_adjust=True, progress=False)
if isinstance(data.columns, pd.MultiIndex):          # newer yfinance returns two-level columns
    data.columns = data.columns.get_level_values(0)
data = data[["Open", "High", "Low", "Close", "Volume"]]
data.index.name = "Date"
data.to_csv(out)
print(f"saved {len(data)} rows, {data.index.min().date()} to {data.index.max().date()} -> {out}")
