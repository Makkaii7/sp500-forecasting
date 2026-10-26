# Data

`sp500_daily.csv` is the S&P 500 index (ticker `^GSPC`), daily, downloaded once with
`download_sp500.py` and committed so that everyone uses the identical file.

Columns: `Date, Open, High, Low, Close, Volume`. Trading days only (no weekends or holidays),
which is why the "missing days" check in part 1 should compare against the exchange calendar,
not against every calendar day.

If the file ever has to be refreshed, say so in the group, re-run the script, and commit the
new file with the date in the commit message. Do not keep two versions.
