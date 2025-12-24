import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed_csv")
OUTPUT_PATH = Path("data/analytics")
OUTPUT_PATH.mkdir(exist_ok=True)

all_data = []

for file in INPUT_PATH.glob("*.csv"):
    df = pd.read_csv(file)

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df = df.drop_duplicates(subset=["date"])

    df["daily_return"] = df["close"].pct_change()

    df["ticker"] = file.stem

    all_data.append(df)

master_df = pd.concat(all_data, ignore_index=True)

master_df.to_csv(OUTPUT_PATH / "daily_returns.csv", index=False)

print("daily_returns.csv created")
print("Total rows:", len(master_df))
print(master_df.head())
