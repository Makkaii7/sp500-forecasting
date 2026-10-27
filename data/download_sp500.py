"""Download the S&P 500 daily series once and save it as data/sp500_daily.csv, with a record of the
source, series identifier, access date, period and sample size (the brief asks for all five).

Run from the repository root:  python data/download_sp500.py
"""
import json
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf

START = "2010-01-01"   # the chosen period: change only by group decision, then commit the new CSV and meta file
TICKER = "^GSPC"       # S&P 500 index on Yahoo Finance

here = Path(__file__).resolve().parent
out = here / "sp500_daily.csv"
data = yf.download(TICKER, start=START, auto_adjust=True, progress=False)
if isinstance(data.columns, pd.MultiIndex):          # newer yfinance returns two-level columns
    data.columns = data.columns.get_level_values(0)
data = data[["Open", "High", "Low", "Close", "Volume"]]
data.index.name = "Date"
data.to_csv(out)

meta = {
    "source": "Yahoo Finance, via the yfinance Python package",
    "source_url": "https://finance.yahoo.com/quote/%5EGSPC/history/",
    "series_identifier": TICKER,
    "series_name": "S&P 500 index, daily, closing value (auto-adjusted)",
    "access_date": date.today().isoformat(),
    "period_requested_from": START,
    "first_date": str(data.index.min().date()),
    "last_date": str(data.index.max().date()),
    "sample_size": int(len(data)),
    "yfinance_version": yf.__version__,
}
(here / "sp500_daily.meta.json").write_text(json.dumps(meta, indent=2))
print(f"saved {len(data)} rows, {meta['first_date']} to {meta['last_date']} -> {out}")
print("source record ->", here / "sp500_daily.meta.json")
