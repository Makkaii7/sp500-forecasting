# S&P 500 forecasting: ARIMA, RNN and LSTM

COSC 621 research report. One shared repository so that all three models and all three
analysis parts run on the same data, the same split and the same metrics.

## Who does what

| Part | Owner | Notebook |
|---|---|---|
| 1. Data preparation (missing values, duplicates, outliers, cleaning, split) | | `notebooks/01_data_preparation.ipynb` |
| 2. Time series analysis (trend, seasonality, ADF/KPSS, ACF/PACF) | | `notebooks/02_time_series_analysis.ipynb` |
| 3. Baseline and evaluation (random walk, MAE, RMSE, plots) | | `notebooks/03_baseline_and_evaluation.ipynb` |
| ARIMA | | `models/arima.ipynb` |
| RNN | | `models/rnn.ipynb` |
| LSTM | | `models/lstm.ipynb` |

Fill in the names once agreed.

## Three rules that make the comparison fair

1. **One data file.** Everyone reads `data/sp500_daily.csv`. It is downloaded once with
   `python data/download_sp500.py` and committed. Nobody re-downloads.
2. **One split.** Train, validation and test dates live in `src/config.py`. Part 2 sets them;
   every model imports them. No shuffling: the data is in time order.
3. **One scorecard.** Metrics come from `src/common.py` (`mae`, `rmse`) and every model saves its
   test-set predictions to `results/<model>_predictions.csv`, so part 3 can compare them in one table.

## Working in Colab or in Cursor

Both edit the same `.ipynb` files.

- **Colab:** File > Open notebook > GitHub tab, paste this repository's URL (tick "Include private
  repos" and authorize once). Save back with File > Save a copy in GitHub.
- **Cursor / VS Code:** clone the repository, create a virtual environment, `pip install -r requirements.txt`,
  open the notebook.

The first code cell of every notebook finds the repository root, so the same notebook runs in both.

## Setup (local)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python data/download_sp500.py    # only once, then commit data/sp500_daily.csv
```

## Target

The models forecast the **daily log return**, `log(close_t / close_{t-1})`, one day ahead.
Predicting the price level makes every model look good because tomorrow's price is almost
today's price; the return is the honest target. `src/config.py` holds this choice in one place.
