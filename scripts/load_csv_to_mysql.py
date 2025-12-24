import pandas as pd
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arvindh*2827",
    database="stock_analysis"
)

cursor = conn.cursor()

# -------- Load daily_returns.csv --------
daily_df = pd.read_csv("data/analytics/daily_returns.csv")
cursor.execute("TRUNCATE TABLE daily_returns")

daily_insert_query = """
INSERT INTO daily_returns
(date, ticker, open, high, low, close, volume, month, daily_return)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

daily_data = [
    (
        row["date"],
        row["ticker"],
        row["open"],
        row["high"],
        row["low"],
        row["close"],
        int(row["volume"]),
        row["month"],
        None if pd.isna(row["daily_return"]) else float(row["daily_return"])
    )
    for _, row in daily_df.iterrows()
]

cursor.executemany(daily_insert_query, daily_data)
conn.commit()

print(f"Inserted {cursor.rowcount} rows into daily_returns")

# -------- Load yearly_summary.csv --------
yearly_df = pd.read_csv("data/analytics/yearly_summary.csv")

cursor.execute("TRUNCATE TABLE yearly_summary")

yearly_insert_query = """
INSERT INTO yearly_summary
(ticker, start_price, end_price, yearly_return_pct, status)
VALUES (%s, %s, %s, %s, %s)
"""

yearly_data = [
    (
        row["ticker"],
        row["start_price"],
        row["end_price"],
        row["yearly_return_pct"],
        row["status"]
    )
    for _, row in yearly_df.iterrows()
]

cursor.executemany(yearly_insert_query, yearly_data)
conn.commit()

print(f"Inserted {cursor.rowcount} rows into yearly_summary")

# -------- Load market_summary.csv --------
market_df = pd.read_csv("data/analytics/market_summary.csv")

cursor.execute("TRUNCATE TABLE market_summary")

market_query = """
INSERT INTO market_summary
(total_stocks, green_stocks, red_stocks, avg_close_price, avg_volume)
VALUES (%s, %s, %s, %s, %s)
"""

market_data = [tuple(market_df.iloc[0])]
cursor.executemany(market_query, market_data)
conn.commit()

print("market_summary loaded")

# -------- Load volatility.csv --------
vol_df = pd.read_csv("data/analytics/volatility.csv")

cursor.execute("TRUNCATE TABLE volatility")

vol_query = """
INSERT INTO volatility (ticker, volatility)
VALUES (%s, %s)
"""

vol_data = [tuple(row) for _, row in vol_df.iterrows()]
cursor.executemany(vol_query, vol_data)
conn.commit()

print("volatility loaded")

# -------- Load cumulative_comparison.csv --------
cum_df = pd.read_csv("data/analytics/cumulative_comparison.csv")

cursor.execute("TRUNCATE TABLE cumulative_comparison")

cum_query = """
INSERT INTO cumulative_comparison
(ticker, start_price, end_price, cumulative_return_pct)
VALUES (%s, %s, %s, %s)
"""

cum_data = [tuple(row) for _, row in cum_df.iterrows()]
cursor.executemany(cum_query, cum_data)
conn.commit()

print("cumulative_comparison loaded")

# -------- Load sector_performance.csv --------
sector_df = pd.read_csv("data/analytics/sector_performance.csv")

cursor.execute("TRUNCATE TABLE sector_performance")

sector_query = """
INSERT INTO sector_performance (sector, avg_sector_return_pct)
VALUES (%s, %s)
"""

sector_data = [tuple(row) for _, row in sector_df.iterrows()]
cursor.executemany(sector_query, sector_data)
conn.commit()

print("sector_performance loaded")

# -------- Load monthly_gainers_losers.csv --------
monthly_df = pd.read_csv("data/analytics/monthly_gainers_losers.csv")

cursor.execute("TRUNCATE TABLE monthly_gainers_losers")

monthly_query = """
INSERT INTO monthly_gainers_losers
(month, ticker, monthly_return_pct, rank_label, category)
VALUES (%s, %s, %s, %s, %s)
"""

monthly_data = [
    (row["month"], row["ticker"], row["monthly_return_pct"], row["rank"], row["category"])
    for _, row in monthly_df.iterrows()
]

cursor.executemany(monthly_query, monthly_data)
conn.commit()

print("monthly_gainers_losers loaded")

print("All data loaded to MySQL database")

# Close cursor and database connection
cursor.close()
conn.close()

