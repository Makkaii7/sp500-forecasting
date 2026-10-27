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

# Split in time order.
# Train: from TRAIN_START up to and including TRAIN_END.
# Validation: after TRAIN_END up to and including VAL_END.
# Test: everything after VAL_END (the most recent 12 months of the data file).
# The data file holds the full history (1927 onwards). TRAIN_START is the period decision the professor
# asked us to justify; Part 2 sets it with evidence (notebook 02, section 0) and the group agrees here.
TRAIN_START = "2010-01-01"   # placeholder until Part 2 decides
TRAIN_END = "2024-10-26"     # validation = the 12 months after this date
VAL_END = "2025-10-26"       # test = everything after this date (12 months)

# Lookback window: how many past days the RNN and LSTM see. A justified choice, see the brief (section 4).
WINDOW = 20

RANDOM_SEED = 42
