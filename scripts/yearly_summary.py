import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/analytics")
OUTPUT_PATH = Path("data/analytics")

df = pd.read_csv(DATA_PATH / "daily_returns.csv")

df["date"] = pd.to_datetime(df["date"])

summary = []

for ticker, group in df.groupby("ticker"):
    group = group.sort_values("date")

    start_price = group.iloc[0]["close"]
    end_price = group.iloc[-1]["close"]

    yearly_return = ((end_price - start_price) / start_price) * 100

    summary.append({
        "ticker": ticker,
        "start_price": round(start_price, 2),
        "end_price": round(end_price, 2),
        "yearly_return_pct": round(yearly_return, 2),
        "status": "Green" if yearly_return > 0 else "Red"
    })

summary_df = pd.DataFrame(summary)
summary_df.to_csv(OUTPUT_PATH / "yearly_summary.csv", index=False)

print("yearly_summary.csv created")
print(summary_df.sort_values("yearly_return_pct", ascending=False).head())
