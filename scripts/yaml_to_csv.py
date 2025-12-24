import yaml
import pandas as pd
from pathlib import Path

RAW_YAML_PATH = Path("data/raw_yaml")
OUTPUT_CSV_PATH = Path("data/processed_csv")

OUTPUT_CSV_PATH.mkdir(exist_ok=True)

all_records = []

yaml_files = list(RAW_YAML_PATH.rglob("*.yaml"))

if not yaml_files:
    raise FileNotFoundError("No YAML files found")

print(f"Total YAML files found: {len(yaml_files)}")

for file_path in yaml_files:
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        all_records.extend(data)

df = pd.DataFrame(all_records)
df["date"] = pd.to_datetime(df["date"])

print("Total records:", len(df))

# Create one CSV per stock
for ticker, group in df.groupby("Ticker"):
    group.sort_values("date").to_csv(
        OUTPUT_CSV_PATH / f"{ticker}.csv",
        index=False
    )

print("Stock-wise CSV files created successfully")
