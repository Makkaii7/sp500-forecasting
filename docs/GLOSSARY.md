# Glossary, in plain words

**Index points.** The unit of the S&P 500 itself. If the index closes at 5,842.3 and we predicted
5,830.0, the error is 12.3 index points. The professor wants all errors in this unit.

**Log return.** How much the index changed from one day to the next, as log(today / yesterday).
Close to the percentage change (0.01 is about +1%). The models work on this because it does not
drift upward the way the price does.

**Target.** The thing a model is trained to predict. Here: tomorrow's log return (internally), turned
back into tomorrow's closing value in index points before scoring.

**Train / validation / test.** Three stretches of time, in order. Train: the model learns here.
Validation: you compare settings here and pick the best. Test: touched once at the very end, to
report the final numbers. The dates are in `src/config.py`.

**Baseline.** The dumbest sensible forecast: tomorrow's close = today's close. Every model must be
compared with it. If a model does not beat it, that is a valid finding, not a failure.

**Random walk.** The idea that each day's value is yesterday's value plus an unpredictable surprise.
If the index is a random walk, the baseline is the best possible forecast.

**MAE.** Mean absolute error: the average size of the mistakes, ignoring direction. In index points here.

**RMSE.** Root mean squared error: like MAE but big mistakes count extra. Also in index points.

**Stationary.** A series that wobbles around a fixed level with a steady spread. The price is not;
the daily return roughly is. ARIMA and the neural networks want a stationary input.

**ADF and KPSS.** Two statistical tests for stationarity. ADF: a small p-value (under 0.05) says
"stationary". KPSS: a small p-value says "not stationary". Read them together.

**ACF and PACF.** Charts of how much each day resembles the days before it (lag 1 = yesterday, lag 2 =
the day before, ...). Bars inside the dashed lines are too small to trust.

**p, d, q (ARIMA).** p = how many past values the model uses, d = how many times the series was
differenced to make it stationary, q = how many past errors it uses.

**Window (lookback).** For the RNN and LSTM: how many past days are fed in to predict the next one.
`config.WINDOW`, default 20.

**Epoch.** One full pass of the training data through a neural network.

**Rolling forecast.** Forecast one day, then move forward one day and forecast again, using only
what was known at that time. The ARIMA notebook does this with `update`; the neural networks do it by
sliding the window.

**Hidden units.** The number of "memory cells" in the RNN or LSTM layer. More units, more capacity,
more risk of overfitting.

**Overfitting.** A model that fits the training period's noise and does worse on new data.
Watch the validation curve; early stopping halts training when validation stops improving.
