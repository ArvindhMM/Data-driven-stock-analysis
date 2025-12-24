import pandas as pd
from pathlib import Path

ANALYTICS_PATH = Path("data/analytics")

# Load daily data
df = pd.read_csv(ANALYTICS_PATH / "daily_returns.csv")

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_results = []

# group by month and ticker
for (month, ticker), group in df.groupby(["month", "ticker"]):
    group = group.sort_values("date")

    start_price = group.iloc[0]["close"]
    end_price = group.iloc[-1]["close"]

    monthly_return = ((end_price - start_price) / start_price) * 100

    monthly_results.append({
        "month": month,
        "ticker": ticker,
        "monthly_return_pct": round(monthly_return, 2)
    })

monthly_df = pd.DataFrame(monthly_results)

final_rows = []

# Get top 5 gainers & losers per month
for month, group in monthly_df.groupby("month"):
    group = group.sort_values("monthly_return_pct", ascending=False)

    top_gainers = group.head(5)
    top_losers = group.tail(5)

    # Add ranks and labels
    for i, row in top_gainers.iterrows():
        final_rows.append({
            "month": row["month"],
            "ticker": row["ticker"],
            "monthly_return_pct": row["monthly_return_pct"],
            "rank": "Top 5",
            "category": "Gainer"
        })

    for i, row in top_losers.iterrows():
        final_rows.append({
            "month": row["month"],
            "ticker": row["ticker"],
            "monthly_return_pct": row["monthly_return_pct"],
            "rank": "Bottom 5",
            "category": "Loser"
        })

final_df = pd.DataFrame(final_rows)

# Save CSV
final_df.to_csv(
    ANALYTICS_PATH / "monthly_gainers_losers.csv",
    index=False
)

print("monthly_gainers_losers.csv created")
print(final_df.head(100))
