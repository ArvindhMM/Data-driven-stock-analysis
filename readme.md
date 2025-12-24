# Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends

## 1. Project Overview

This project analyzes the performance of 50 stocks over a one-year period using historical market data.  
The objective is to clean, organize, analyze, and visualize stock market trends to support data-driven investment and analytical decisions.

The project implements an end-to-end data analytics workflow using Python for data processing, MySQL for data storage, Streamlit for interactive dashboards, and Power BI for business intelligence reporting.

---

## 2. Objectives

1. Analyze daily stock price movements including Open, High, Low, Close, and Volume  
2. Identify top-performing and worst-performing stocks on a yearly basis  
3. Analyze sector-wise stock performance  
4. Measure stock volatility for risk assessment  
5. Identify monthly top gainers and losers  
6. Study correlations between stock prices  
7. Deliver insights using interactive dashboards  

---

## 3. Business Use Cases

1. Stock Performance Ranking  
   - Identify top gainers and losers yearly and monthly  

2. Market Overview  
   - Understand overall market sentiment using green vs red stock distribution  

3. Risk Assessment  
   - Identify high-risk stocks using volatility analysis  

4. Sector Analysis  
   - Compare industry-level performance  

5. Decision Support  
   - Support retail and institutional investors with actionable insights  

---

## 4. Dataset Description

- Data provided in YAML format  
- Organized month-wise  
- Each YAML file contains daily stock data  
- Data converted into CSV format for analysis  
- Final analytical datasets stored in MySQL  

---

## 5. Data Processing Workflow

1. Extract raw YAML data  
2. Clean and standardize stock data  
3. Generate analytical datasets:
   - Daily returns  
   - Yearly summary  
   - Market summary  
   - Sector performance  
   - Volatility metrics  
   - Monthly gainers and losers  
4. Load processed data into MySQL  
5. Visualize insights using Streamlit and Power BI  

---

## 6. Key Metrics and Analysis

### 6.1 Market Overview
- Total number of stocks  
- Green vs red stocks  
- Average closing price  
- Average trading volume  

### 6.2 Yearly Performance
- Top 10 gainers  
- Top 10 losers  
- Yearly return percentage  

### 6.3 Sector-wise Performance
- Average yearly return by sector  

### 6.4 Volatility Analysis
- Standard deviation of daily returns  
- Identification of high-risk stocks  

### 6.5 Monthly Gainers and Losers
- Top 5 gainers per month  
- Top 5 losers per month  

### 6.6 Correlation Analysis
- Correlation matrix of stock closing prices  
- Identification of stock movement relationships  

---

## 7. Technologies Used

### 7.1 Programming Language
- Python  

### 7.2 Libraries
- Pandas  
- NumPy  
- Matplotlib  
- SQLAlchemy  
- MySQL Connector  
- Streamlit  

### 7.3 Database
- MySQL  

### 7.4 Visualization Tools
- Streamlit  
- Power BI  

## 8. How to Run the Project

### 8.1 Python Setup

Create a virtual environment:

```bash
python -m venv venv
```
Activate the virtual environment:

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```
### 8.2 Run Data Processing Scripts
Run the following scripts in order:

```bash
python scripts/yaml_to_csv.py
python scripts/daily_returns.py
python scripts/yearly_summary.py
python scripts/market_summary.py
python scripts/sector_performance.py
python scripts/monthly_gainers_losers.py
python scripts/cumulative_comparison.py
python scripts/correlation_analysis.py
python scripts/volatility_analysis.py
```
### 8.3 Load Data into MySQL
Create a database named stock_analysis

Load CSV data into MySQL using:

```bash
python scripts/load_csv_to_mysql.py
```
### 8.4 Run Streamlit Application
```bash
streamlit run streamlit_app/app.py
```
### 8.5 Power BI Dashboard
1. Open Power BI Desktop

2. Connect to the MySQL database

3. Load required tables

4. Explore interactive dashboards

## 9. Power BI Dashboard Pages
1. Market Overview

2. Yearly Gainers and Losers

3. Sector-wise Performance

4. Volatility Analysis

5. Monthly Gainers and Losers

## 10. Key Insights
1. Majority of stocks showed positive yearly performance

2. Certain sectors significantly outperformed the overall market

3. Volatility analysis highlighted high-risk stocks

4. Correlation analysis revealed sector-based clustering