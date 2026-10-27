# Start here

You only need to do three things: open your notebook, run it, save it back. Pick the tool you like.
No git knowledge is needed for the Colab route.

## Route A: Google Colab (nothing to install)

### One-time setup, about 5 minutes

1. Accept the GitHub invitation you received by email, then sign in at github.com.
2. Make a token so Colab can read this private repository. On github.com: your profile picture (top
   right) > Settings > Developer settings (bottom of the left menu) > Personal access tokens >
   **Tokens (classic)** > Generate new token (classic). Note: `colab`. Expiration: 90 days.
   Tick the box **repo**. Click Generate token and copy it (it is shown once).
   It must be a classic token: the "fine-grained" kind cannot read a repository owned by someone else.
3. In Colab (colab.research.google.com), click the key icon in the left sidebar (Secrets). Add a
   secret with the name `GITHUB_TOKEN`, paste the token as the value, and switch "Notebook access" on.
   Colab remembers it for all your notebooks, so the setup cell will never ask you for it.

### Every time you work

1. In Colab: File > Open notebook > the **GitHub** tab. Paste `https://github.com/Makkaii7/sp500-forecasting`
   and tick **Include private repos** (the first time, a GitHub window asks you to authorize Colab: accept).
   Click your notebook in the list.
2. Run the first code cell, called Setup. It fetches the repository and the data into your Colab session.
   The first run takes about a minute.
3. Work. Run a cell with Shift+Enter. Run the cells in order, top to bottom.
4. Save back: File > **Save a copy in GitHub**. Repository: `Makkaii7/sp500-forecasting`. File path: exactly
   the one you opened (for example `models/arima.ipynb`). Write a short message, click OK. Done: that
   is your "push".

### When your model is finished (model notebooks only)

The last cell of your model notebook downloads two small files, `<model>_predictions.csv` and
`<model>_meta.json`. Put them in the repository so part 3 can read them: on github.com open the
`results` folder > Add file > Upload files > drop the two files > Commit changes.

## Route B: Cursor or VS Code (runs on your computer)

### One-time setup

1. Install Python 3.11 or 3.12 and git if you do not have them.
2. In a terminal:
   ```
   git clone https://github.com/Makkaii7/sp500-forecasting.git
   cd sp500-forecasting
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Open the folder in Cursor or VS Code and open your notebook. When asked for a kernel, pick `.venv`.

### Every time you work

1. `git pull` (gets what the others saved).
2. Run the first code cell, then work.
3. Save back:
   ```
   git add models/lstm.ipynb              # your own file; add results/lstm_* too when the model is done
   git commit -m "LSTM: first configurations"
   git push
   ```

## Rules of the road

- Edit **your own notebook** only. If you think a shared file (`src/config.py`, `src/common.py`, the
  data) should change, say so in the group first.
- Never shuffle the data, and never run your model on the test period until the very end.
- Run cells in order. If something looks odd, Runtime > Restart session, then run from the top.
- Stuck? See [TROUBLESHOOTING.md](TROUBLESHOOTING.md). Unknown word? See [GLOSSARY.md](GLOSSARY.md).
