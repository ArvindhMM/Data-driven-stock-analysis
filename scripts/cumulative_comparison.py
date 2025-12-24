import pandas as pd
from pathlib import Path

ANALYTICS_PATH = Path("data/analytics")

# Load daily data
df = pd.read_csv(ANALYTICS_PATH / "daily_returns.csv")
df["date"] = pd.to_datetime(df["date"])

results = []

for ticker, group in df.groupby("ticker"):
    group = group.sort_values("date")

    start_price = group.iloc[0]["close"]
    end_price = group.iloc[-1]["close"]

    cumulative_return = ((end_price - start_price) / start_price) * 100

    results.append({
        "ticker": ticker,
        "start_price": round(start_price, 2),
        "end_price": round(end_price, 2),
        "cumulative_return_pct": round(cumulative_return, 2)
    })

cumulative_df = pd.DataFrame(results)

# Sort by best performers
cumulative_df = cumulative_df.sort_values(
    "cumulative_return_pct", ascending=False
)

# Save CSV
cumulative_df.to_csv(
    ANALYTICS_PATH / "cumulative_comparison.csv",
    index=False
)

print("cumulative_comparison.csv created")
print(cumulative_df.head())
