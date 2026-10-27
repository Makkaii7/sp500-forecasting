# Working in Cursor or VS Code (on your own computer)

## One-time setup

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

## Every time you work

1. `git pull` (gets what the others saved).
2. Run the first cell, then work.
3. Save back:
   ```
   git add models/lstm.ipynb              # your own file; add results/lstm_* too when the model is done
   git commit -m "LSTM: first configurations"
   git push
   ```

The rules in [START_HERE.md](START_HERE.md) apply here too.
