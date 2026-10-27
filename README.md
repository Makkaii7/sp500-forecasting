# S&P 500 forecasting: ARIMA, RNN and LSTM against a random-walk baseline

COSC 621 research report. Three models, three analysis parts, one shared repository, so that
everything runs on the same data, the same split and the same scorecard.

**New here? Read [docs/START_HERE.md](docs/START_HERE.md).** Three steps, nothing to install or set up.

## The map

```
sp500-forecasting/
├── data/            the S&P 500 file everyone uses: full history from 1927 (already downloaded, do not re-download)
├── notebooks/       part 1 (data check), part 2 (time series analysis), part 3 (baseline and evaluation)
├── models/          arima.ipynb, rnn.ipynb, lstm.ipynb  (one per person)
├── src/             config.py (the shared settings) and common.py (shared helper functions)
├── results/         every model saves its test predictions here; part 3 reads them
├── report/          the LaTeX report skeleton with the sections the professor asked for
└── docs/            START_HERE, CURSOR, GLOSSARY, TROUBLESHOOTING
```

## Who does what

| Part | Owner | Notebook | Open |
|---|---|---|---|
| 1. Data collection and preparation | | `notebooks/01_data_preparation.ipynb` | [Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/notebooks/01_data_preparation.ipynb) |
| 2. Time series analysis (training data only) | | `notebooks/02_time_series_analysis.ipynb` | [Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/notebooks/02_time_series_analysis.ipynb) |
| 3. Baseline and evaluation | | `notebooks/03_baseline_and_evaluation.ipynb` | [Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/notebooks/03_baseline_and_evaluation.ipynb) |
| ARIMA | | `models/arima.ipynb` | [Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/models/arima.ipynb) |
| Vanilla RNN | | `models/rnn.ipynb` | [Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/models/rnn.ipynb) |
| LSTM | | `models/lstm.ipynb` | [Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/models/lstm.ipynb) |
| Report (LaTeX) | everyone, own sections | `report/main.tex` | |

Order of work: parts 1 and 2 first (part 2 confirms the split dates), then the three models, then part 3.

## Three rules, in plain words

1. **One data file.** Everyone reads `data/sp500_daily.csv`, the full history from 1927, already in the
   repository with a record of where it came from (`data/sp500_daily.meta.json`). Nobody downloads it again.
   The years the models train on are a setting (`TRAIN_START` in `src/config.py`), chosen by Part 2 with
   evidence (notebook 02, section 0), because the professor asked for a justified period, not a preference.
2. **One split.** The dates that separate training, validation and test live in `src/config.py`:
   test = the last 12 months of the file, validation = the 12 months before. Every notebook imports them.
   Time order only, never shuffled.
   Tune your model on validation; run it on test exactly once, at the end.
3. **One scorecard.** The models work on the daily return, but every forecast is turned back into a
   closing value in index points by `common.save_predictions(...)` before it is scored, because the
   professor wants MAE and RMSE in index points against the "tomorrow equals today" baseline.
   You never compute this yourself; you call the helper and it does it.

## What the brief asks for, and where it lives

| Brief section | Where |
|---|---|
| 1 Data: source record, period, order, duplicates, closures vs missing, outliers | notebook 01, `data/sp500_daily.meta.json`; period justification: notebook 02 section 0 |
| 2 Analysis on training data: trend, seasonality, ADF/KPSS, ACF/PACF, random walk definition | notebook 02 |
| 3 Design: next-day close, conversion from returns, chronological split, rolling forecasts | `src/config.py`, `src/common.py`, each model notebook |
| 4 Methods: mechanism, equations, p/d/q justification, gates, configuration tables | each model notebook |
| 5 Evaluation: baseline, MAE and RMSE in index points, plots, residuals, cost, meaningfulness | notebook 03 |
| 6 Report structure | `report/main.tex` |
| 7 Submission: zip with PDF, runnable code, README with versions, seeds, data access | this README, `requirements-lock.txt`, `src/config.py` (seed) |

## Reproducibility (for the submission)

- Random seed: `config.RANDOM_SEED`, used by every model notebook.
- Package versions: `requirements-lock.txt` (made with `pip freeze > requirements-lock.txt` before submitting).
- Data access: `data/download_sp500.py` and `data/sp500_daily.meta.json`.
- Order to run: 01, 02, then arima / rnn / lstm, then 03.

## Submission checklist (brief, section 7)

- [ ] one `.zip`: the PDF report, this repository (runnable notebooks), this README
- [ ] all members' names and student IDs in the report
- [ ] README states setup, execution order, package versions, random seeds, data access
- [ ] every figure and table is explained in the text (code output alone is insufficient)
- [ ] data, methods and adapted code are cited
