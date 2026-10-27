# Troubleshooting

Read the **last line** of an error message first; it is the one that matters.

**`ModuleNotFoundError: No module named 'src'`** – you ran a cell before the Setup cell, or you opened the
notebook from the wrong folder. Run the Setup cell (the first code cell) again.

**`ModuleNotFoundError: No module named 'pmdarima'` (or statsmodels, keras, ...)** – the Setup cell
installs what the notebook needs, so run it again. If it still fails, add a cell with
`!pip install -r requirements.txt` and run it once. On your own computer: `pip install -r requirements.txt`
inside the `.venv`.

**Colab says "You must restart the runtime" after installing** – Runtime > Restart session, then run the
Setup cell again. It will not need to install a second time.

**Colab asks for a GitHub token every time** – add it as a Colab secret named `GITHUB_TOKEN` (key icon
in the left sidebar) with "Notebook access" switched on. See START_HERE.

**`fatal: could not read Username`, `Repository not found` or `Authentication failed` in the Setup
cell** – the token cannot see the repository. It must be a **classic** token with the `repo` box ticked
(a fine-grained token does not work for a repository owned by someone else), and you must have accepted
the invitation. Make a new one and update the Colab secret.

**The GitHub tab in Colab does not list the repository** – tick "Include private repos" and accept the
authorization window; make sure you are signed in to the right GitHub account.

**`FileNotFoundError: data/sp500_daily.csv`** – the Setup cell did not finish. In Colab, run it again.
On your computer, make sure you opened the repository folder itself, not a subfolder.

**My numbers are different from a teammate's** – normal for the neural networks: different machine,
different package versions. The seed in `src/config.py` makes a single machine repeatable, not every
machine identical. Report the versions you used (`pip freeze`).

**The ARIMA rolling-forecast cell is slow** – it updates the model for every day of the validation or test
period. A few minutes is expected. Do not stop it halfway.

**"Save a copy in GitHub" created a new file instead of updating mine** – the file path in the save
dialog was changed. Use exactly the path of the notebook you opened (for example `models/rnn.ipynb`).

**Part 3 does not show my model** – the two result files are not in the repository's `results` folder
yet. See START_HERE, "When your model is finished".

**Something else** – paste the full error message in the group.
