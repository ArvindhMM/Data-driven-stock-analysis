import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# -----------------------------
# MySQL Connection Function
# -----------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arvindh*2827",
        database="stock_analysis"
    )

st.set_page_config(page_title="Stock Performance Dashboard", layout="wide")

st.title("📈 Data-Driven Stock Performance Dashboard")

# -----------------------------
# Market Summary Section
# -----------------------------
st.header("📊 Market Overview")

conn = get_connection()
market_df = pd.read_sql("SELECT * FROM market_summary", conn)
conn.close()

col1, col2, col3 = st.columns(3)
colb1, colb2 = st.columns(2)

col1.metric("Total Stocks", int(market_df["total_stocks"][0]))
col2.metric("Green Stocks", int(market_df["green_stocks"][0]))
col3.metric("Red Stocks", int(market_df["red_stocks"][0]))

colb1.metric("Average Close Price", round(market_df["avg_close_price"][0], 2))
colb2.metric("Average Volume", int(market_df["avg_volume"][0]))


# -----------------------------
# Yearly Top Gainers & Losers
# -----------------------------
st.header("🏆 Yearly Top Gainers & Losers")

conn = get_connection()
yearly_df = pd.read_sql("SELECT * FROM yearly_summary", conn)
conn.close()

# Sort data
top_gainers = yearly_df.sort_values("yearly_return_pct", ascending=False).head(10)
top_losers = yearly_df.sort_values("yearly_return_pct").head(10)

col1, col2 = st.columns(2)

# Top Gainers
with col1:
    st.subheader("🟢 Top 10 Gainers")
    st.bar_chart(
        top_gainers.set_index("ticker")["yearly_return_pct"]
    )

# Top Losers
with col2:
    st.subheader("🔴 Top 10 Losers")
    st.bar_chart(
        top_losers.set_index("ticker")["yearly_return_pct"]
    )



# -----------------------------
# Volatility Analysis
# -----------------------------
st.header("⚠️ Volatility Analysis (Top 10 Most Volatile Stocks)")

conn = get_connection()
vol_df = pd.read_sql(
    "SELECT * FROM volatility ORDER BY volatility DESC LIMIT 10",
    conn
)
conn.close()

# Set ticker as index for better chart labeling
vol_df = vol_df.set_index("ticker")

st.bar_chart(vol_df["volatility"])

# -----------------------------
# Cumulative Return Comparison
# -----------------------------
st.header("📊 Cumulative Return Comparison")

conn = get_connection()

cum_df = pd.read_sql(
    """
    SELECT ticker, cumulative_return_pct
    FROM cumulative_comparison
    ORDER BY cumulative_return_pct DESC
    """,
    conn
)

conn.close()

top_cum_df = cum_df.set_index("ticker")

st.bar_chart(top_cum_df["cumulative_return_pct"])

# -----------------------------
# Sector-wise Performance
# -----------------------------
st.header("🏭 Sector-wise Performance")

conn = get_connection()
sector_df = pd.read_sql(
    "SELECT * FROM sector_performance ORDER BY avg_sector_return_pct DESC",
    conn
)
conn.close()

st.bar_chart(
    sector_df.set_index("sector")["avg_sector_return_pct"]
)

# -----------------------------
# Stock Price Correlation Heatmap
# -----------------------------
st.header("🔗 Stock Price Correlation Heatmap")

st.info(
    "This heatmap shows how stock prices move together. "
    "Darker colors indicate stronger correlations."
)

conn = get_connection()

# Fetch closing prices
corr_df = pd.read_sql(
    "SELECT date, ticker, close FROM daily_returns",
    conn
)

conn.close()

# Prepare data
corr_df["date"] = pd.to_datetime(corr_df["date"])

# Pivot: rows = date, columns = ticker, values = close price
pivot_df = corr_df.pivot(
    index="date",
    columns="ticker",
    values="close"
)

# Calculate correlation matrix
correlation_matrix = pivot_df.corr()

# Plot heatmap
fig, ax = plt.subplots(figsize=(14, 10))
cax = ax.imshow(correlation_matrix)

ax.set_title("Stock Price Correlation Heatmap", fontsize=14)

ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=90)

ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_yticklabels(correlation_matrix.columns)

fig.colorbar(cax)

plt.tight_layout()
st.pyplot(fig)

# -----------------------------
# Monthly Top 5 Gainers & Losers
# -----------------------------
st.header("📅 Monthly Top 5 Gainers & Losers")

conn = get_connection()

# Get available months for dropdown
months_df = pd.read_sql(
    "SELECT DISTINCT month FROM monthly_gainers_losers ORDER BY month",
    conn
)

month_list = months_df["month"].tolist()

# Month selector
selected_month = st.selectbox("Select Month", month_list)

# Fetch data for selected month
monthly_df = pd.read_sql(
    f"""
    SELECT ticker, monthly_return_pct, category
    FROM monthly_gainers_losers
    WHERE month = '{selected_month}'
    """,
    conn
)

conn.close()

# Split gainers and losers
gainers_df = monthly_df[monthly_df["category"] == "Gainer"] \
    .set_index("ticker")

losers_df = monthly_df[monthly_df["category"] == "Loser"] \
    .set_index("ticker")

col1, col2 = st.columns(2)

# Gainers chart
with col1:
    st.subheader("🟢 Top 5 Gainers")
    st.bar_chart(gainers_df["monthly_return_pct"])

# Losers chart
with col2:
    st.subheader("🔴 Top 5 Losers")
    st.bar_chart(losers_df["monthly_return_pct"])
