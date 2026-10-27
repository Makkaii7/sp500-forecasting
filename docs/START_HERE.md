# Start here

Nothing to install, nothing to set up. You need a Google account (for Colab) and to have accepted
the GitHub invitation from your email.

## Every time you work: three steps

**1. Click your notebook.** It opens in Colab.

| Part | Click |
|---|---|
| Part 1, data preparation | [open in Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/notebooks/01_data_preparation.ipynb) |
| Part 2, time series analysis | [open in Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/notebooks/02_time_series_analysis.ipynb) |
| Part 3, baseline and evaluation | [open in Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/notebooks/03_baseline_and_evaluation.ipynb) |
| ARIMA | [open in Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/models/arima.ipynb) |
| RNN | [open in Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/models/rnn.ipynb) |
| LSTM | [open in Colab](https://colab.research.google.com/github/Makkaii7/sp500-forecasting/blob/main/models/lstm.ipynb) |

**2. Run the first cell** (click in it, press Shift+Enter). It fetches the data and the shared code.
Wait for the green tick, then continue cell by cell, top to bottom.

**3. When you stop: File > Save a copy in GitHub > OK.** Keep the file path it shows. The first time,
GitHub asks you to allow Colab: click Authorize.

Why steps 2 and 3 every time? Colab is a borrowed computer that is wiped when you close it. Step 2 brings
the files back, step 3 saves your work.

## When your model is finished (ARIMA, RNN, LSTM only)

The last cell of your notebook downloads two small files. On github.com open the `results` folder >
Add file > Upload files > drop them in > Commit changes. Part 3 reads them from there.

## Rules

- Work in your own notebook only. The shared files (`src`, `data`) change only if the group agrees.
- Never shuffle the data, and never run on the test period until the very end.
- Something broke? Runtime > Restart session, then run from the top. Still broken? [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
  Unknown word? [GLOSSARY.md](GLOSSARY.md).

Prefer Cursor or VS Code on your own computer? [CURSOR.md](CURSOR.md).
