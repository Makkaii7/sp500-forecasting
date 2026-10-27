# Troubleshooting

Read the **last line** of an error message first; it is the one that matters.

**The link opens "Notebook not found" or a blank page** – sign in to your Google account, then click the
link again.

**`ModuleNotFoundError: No module named 'src'`** – you ran a cell before the first (Setup) cell. Run the
Setup cell, then continue.

**`ModuleNotFoundError: No module named 'pmdarima'` (or statsmodels, keras, ...)** – the Setup cell
installs what the notebook needs; run it again. On your own computer: `pip install -r requirements.txt`
inside the `.venv`.

**Colab says "You must restart the runtime"** – Runtime > Restart session, then run the Setup cell again.

**`FileNotFoundError: data/sp500_daily.csv`** – the Setup cell did not finish. Run it again. On your own
computer, make sure you opened the repository folder itself, not a subfolder.

**"Save a copy in GitHub" does not list the repository** – accept the GitHub invitation from your email
first, then try again.

**"Save a copy in GitHub" created a new file instead of updating mine** – the file path in the dialog
was changed. Use exactly the path of the notebook you opened (for example `models/rnn.ipynb`).

**My numbers are different from a teammate's** – normal for the neural networks: different machine,
different package versions. The seed in `src/config.py` makes one machine repeatable, not every machine
identical. Report the versions you used (`pip freeze`).

**The ARIMA rolling-forecast cell is slow** – it updates the model for every day of the period. A few
minutes is expected. Do not stop it halfway.

**Part 3 does not show my model** – the two result files are not in the repository's `results` folder
yet. See START_HERE, "When your model is finished".

**Something else** – paste the full error message in the group.
