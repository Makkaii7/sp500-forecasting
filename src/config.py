"""Single source of truth for the choices every notebook must share.

Part 2 (time series analysis) sets the split dates after looking at the data.
Everyone else imports them. Change them here only, by group decision.
"""

DATA_FILE = "data/sp500_daily.csv"

# What the models forecast, one day ahead.
# "log_return": log(close_t / close_{t-1})   <- recommended (stationary, honest)
# "close":      the price level                <- only as a comparison, see README
TARGET = "log_return"

# Split in time order. Train: up to and including TRAIN_END.
# Validation: after TRAIN_END up to and including VAL_END. Test: everything after VAL_END.
TRAIN_END = "2022-12-31"   # placeholder, to be confirmed by part 2
VAL_END = "2023-12-31"     # placeholder, to be confirmed by part 2

# Window of past days fed to the RNN and LSTM (and to any lag-based features).
WINDOW = 20

RANDOM_SEED = 42
