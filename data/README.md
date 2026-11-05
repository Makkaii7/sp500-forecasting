# Data

`sp500_daily.csv` is the S&P 500 index (ticker `^GSPC`), one row per trading day, downloaded once with
`download_sp500.py` and saved here so that everyone uses the identical file. Do not download it again.

Columns: `Date, Open, High, Low, Close, Volume`. Weekends and market holidays are not in the file,
because the market was closed; that is correct, not missing data.

`sp500_daily.meta.json` records where the data came from, the identifier, the access date, the period
and the number of rows. Part 1 prints it and the report cites it.

If the file ever has to be refreshed, say so in the group first, re-run `python data/download_sp500.py`
from the repository folder, and commit both files with the date in the commit message. Never keep two versions.

## The three sets, as files

`splits/train.csv`, `splits/validation.csv` and `splits/test.csv` are the training, validation and test
sets (Date, Close, log_return), cut from `sp500_daily.csv` with the dates in `src/config.py` by
`make_splits.py`. They are there for anyone who wants to open and check the data. The notebooks do not
read them: the setup cell makes the same three sets itself, so there is only one place where the split is
defined. If the dates in `src/config.py` change, run `python data/make_splits.py` again and commit the files.
