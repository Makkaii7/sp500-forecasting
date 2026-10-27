# S&P 500 forecasting: ARIMA, RNN and LSTM against a random-walk baseline

COSC 621 research report (the brief: "Time Series Forecasting Research Project", weight 20%).
One shared repository so that all three models and all three analysis parts run on the same data,
the same chronological split, the same one-day horizon and the same scorecard in index points.

## Who does what

| Part | Owner | Notebook |
|---|---|---|
| 1. Data collection and preparation | | `notebooks/01_data_preparation.ipynb` |
| 2. Time series analysis (training data only) | | `notebooks/02_time_series_analysis.ipynb` |
| 3. Baseline and evaluation | | `notebooks/03_baseline_and_evaluation.ipynb` |
| ARIMA | | `models/arima.ipynb` |
| Vanilla RNN | | `models/rnn.ipynb` |
| LSTM | | `models/lstm.ipynb` |
| Report (LaTeX) | everyone, own sections | `report/main.tex` |

## Three rules that make the comparison fair

1. **One data file.** Everyone reads `data/sp500_daily.csv`. It is downloaded once with
   `python data/download_sp500.py`, which also writes `data/sp500_daily.meta.json` (source URL,
   series identifier, access date, period, sample size). Both files are committed. Nobody re-downloads.
2. **One split.** Train, validation and test dates live in `src/config.py`. Part 2 sets them;
   every model imports them. Chronological, no shuffling. Models are tuned on validation only and
   touch the test set once.
3. **One scorecard, in index points.** The models may work on daily log returns (`config.TARGET`), but
   every forecast is converted back to a closing value with `common.to_price` before it is scored.
   `common.save_predictions` writes each model's test predictions and a small JSON with its settings and
   training time to `results/`; part 3's `common.scorecard()` reads them all and compares them with the
   last-observed-value baseline on identical test dates.

## What the brief asks for, and where it lives

| Brief section | Where |
|---|---|
| 1 Data: source record, period, order, duplicates, closures vs missing, outliers | notebook 01, `data/sp500_daily.meta.json` |
| 2 Analysis on training data: trend, seasonality, ADF/KPSS, ACF/PACF, random walk definition | notebook 02 |
| 3 Design: next-day close, conversion from returns, chronological split, rolling forecasts | `src/config.py`, `src/common.py`, each model notebook |
| 4 Methods: mechanism, equations, p/d/q justification, gates, configuration tables | each model notebook, section "configurations" |
| 5 Evaluation: baseline, MAE and RMSE in index points, plots, residuals, cost, meaningfulness | notebook 03 |
| 6 Report structure | `report/main.tex` |
| 7 Submission: zip with PDF, runnable code, README with versions, seeds, data access | this README, `requirements-lock.txt`, `src/config.py` (seed) |

## Working in Colab or in Cursor

Both edit the same `.ipynb` files.

- **Colab:** File > Open notebook > GitHub tab, paste this repository's URL (tick "Include private
  repos" and authorize once). Save back with File > Save a copy in GitHub.
- **Cursor / VS Code:** clone, create a virtual environment, `pip install -r requirements.txt`, open the notebook.

The first code cell of every notebook finds the repository root (and clones it in Colab), so the same
notebook runs in both.

## Setup (local)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python data/download_sp500.py    # only once, then commit data/sp500_daily.csv and data/sp500_daily.meta.json
pip freeze > requirements-lock.txt   # exact package versions for the submission README
```

## Reproducibility

- Random seed: `config.RANDOM_SEED` (used by Keras in every model notebook).
- Package versions: `requirements-lock.txt` (generate it with the command above before submitting).
- Data access: `data/download_sp500.py` and `data/sp500_daily.meta.json`.
- Order to run: 01, 02 (sets the split dates), then the three model notebooks, then 03.

## Submission checklist (brief, section 7)

- [ ] one `.zip`: the PDF report, this repository (runnable notebooks), this README
- [ ] all members' names and student IDs in the report
- [ ] README states setup, execution order, package versions, random seeds, data access
- [ ] every figure and table is explained in the text (code output alone is insufficient)
- [ ] data, methods and adapted code are cited
