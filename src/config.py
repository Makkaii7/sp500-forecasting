"""Single source of truth for the choices every notebook must share.

Part 2 (time series analysis) sets the split dates after looking at the data.
Everyone else imports them. Change them here only, by group decision.
"""

DATA_FILE = "data/sp500_daily.csv"

# What the models work on internally, one day ahead.
# "log_return": log(close_t / close_{t-1})   <- recommended: stationary, so the models have something to learn
# "close":      the price level
# Whatever the models work on, EVERY forecast is converted back to a closing value in index points
# before it is scored (common.to_price), because the brief asks for MAE and RMSE in index points
# against a last-observed-value baseline on identical test dates.
TARGET = "log_return"

# Split in time order. Train: up to and including TRAIN_END.
# Validation: after TRAIN_END up to and including VAL_END. Test: everything after VAL_END.
TRAIN_END = "2022-12-31"   # placeholder, to be confirmed by part 2
VAL_END = "2023-12-31"     # placeholder, to be confirmed by part 2

# Lookback window: how many past days the RNN and LSTM see. A justified choice, see the brief (section 4).
WINDOW = 20

RANDOM_SEED = 42
