import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ANALYTICS_PATH = Path("data/analytics")

# Load daily data
df = pd.read_csv(ANALYTICS_PATH / "daily_returns.csv")

df["date"] = pd.to_datetime(df["date"])

# Pivot data: rows = date, columns = ticker, values = close price
pivot_df = df.pivot(
    index="date",
    columns="ticker",
    values="close"
)

print("Pivot table created")
print(pivot_df.head())

# Calculate correlation matrix
corr_matrix = pivot_df.corr()

print("Correlation matrix created")
print(corr_matrix.head())

plt.figure(figsize=(14, 10))

plt.imshow(corr_matrix)
plt.colorbar()

plt.title("Stock Price Correlation Heatmap")

plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

plt.tight_layout()
plt.show()

