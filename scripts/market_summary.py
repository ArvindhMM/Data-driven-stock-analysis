import pandas as pd
from pathlib import Path

ANALYTICS_PATH = Path("data/analytics")

# Load datasets
daily_df = pd.read_csv(ANALYTICS_PATH / "daily_returns.csv")
yearly_df = pd.read_csv(ANALYTICS_PATH / "yearly_summary.csv")

# Green vs Red count
green_count = (yearly_df["status"] == "Green").sum()
red_count = (yearly_df["status"] == "Red").sum()
total_stocks = len(yearly_df)

# Average price & volume (across all stocks & days)
avg_price = daily_df["close"].mean()
avg_volume = daily_df["volume"].mean()

# Create summary dataframe
summary_df = pd.DataFrame([{
    "total_stocks": total_stocks,
    "green_stocks": green_count,
    "red_stocks": red_count,
    "avg_close_price": round(avg_price, 2),
    "avg_volume": round(avg_volume, 0)
}])

# Save CSV
summary_df.to_csv(ANALYTICS_PATH / "market_summary.csv", index=False)

print("market_summary.csv created")
print(summary_df)
