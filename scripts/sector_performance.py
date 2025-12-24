import pandas as pd
from pathlib import Path

ANALYTICS_PATH = Path("data/analytics")
SECTOR_PATH = Path("data/sector_data")

# Load yearly stock performance
yearly_df = pd.read_csv(ANALYTICS_PATH / "yearly_summary.csv")

# Load sector data
sector_df = pd.read_csv(SECTOR_PATH / "Sector_data.csv")

# Extract ticker from Symbol
sector_df["ticker"] = sector_df["Symbol"].str.split(":").str[-1].str.strip()

# Keep required columns
sector_df = sector_df[["ticker", "COMPANY", "sector"]]

# Merge with yearly performance
merged_df = yearly_df.merge(
    sector_df,
    on="ticker",
    how="left"
)

# Calculate average sector performance
sector_perf = (
    merged_df
    .groupby("sector")["yearly_return_pct"]
    .mean()
    .reset_index()
    .rename(columns={"yearly_return_pct": "avg_sector_return_pct"})
    .sort_values("avg_sector_return_pct", ascending=False)
)

# Save CSV
sector_perf.to_csv(
    ANALYTICS_PATH / "sector_performance.csv",
    index=False
)

print("sector_performance.csv created")
print(sector_perf)
