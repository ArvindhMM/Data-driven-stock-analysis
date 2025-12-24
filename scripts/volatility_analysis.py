import pandas as pd
from pathlib import Path

ANALYTICS_PATH = Path("data/analytics")

# Load daily returns data
df = pd.read_csv(ANALYTICS_PATH / "daily_returns.csv")

# Remove first-day NaN returns
df = df.dropna(subset=["daily_return"])

volatility_data = []

for ticker, group in df.groupby("ticker"):
    volatility = group["daily_return"].std()

    volatility_data.append({
        "ticker": ticker,
        "volatility": round(volatility, 6)
    })

volatility_df = pd.DataFrame(volatility_data)

# Sort by highest volatility
volatility_df = volatility_df.sort_values("volatility", ascending=False)

# Save CSV
volatility_df.to_csv(ANALYTICS_PATH / "volatility.csv", index=False)

print("volatility.csv created")
print(volatility_df.head(10))
