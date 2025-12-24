USE stock_analysis;

CREATE TABLE daily_returns (
    date DATE,
    ticker VARCHAR(20),
    open DECIMAL(10,2),
    high DECIMAL(10,2),
    low DECIMAL(10,2),
    close DECIMAL(10,2),
    volume BIGINT,
    month VARCHAR(7),
    daily_return DECIMAL(10,6)
);

CREATE TABLE yearly_summary (
    ticker VARCHAR(20) PRIMARY KEY,
    start_price DECIMAL(10,2),
    end_price DECIMAL(10,2),
    yearly_return_pct DECIMAL(6,2),
    status VARCHAR(10)
);
USE stock_analysis;

TRUNCATE TABLE daily_returns;
TRUNCATE TABLE yearly_summary;
TRUNCATE TABLE market_summary;
TRUNCATE TABLE volatility;
TRUNCATE TABLE cumulative_comparison;
TRUNCATE TABLE sector_performance;
TRUNCATE TABLE monthly_gainers_losers;
TRUNCATE TABLE correlation_matrix;

SELECT COUNT(*) FROM daily_returns;
SELECT COUNT(*) FROM yearly_summary;
SELECT COUNT(*) FROM market_summary;
SELECT COUNT(*) FROM volatility;
SELECT COUNT(*) FROM cumulative_comparison;
SELECT COUNT(*) FROM sector_performance;
SELECT COUNT(*) FROM monthly_gainers_losers;

CREATE TABLE market_summary (
    total_stocks INT,
    green_stocks INT,
    red_stocks INT,
    avg_close_price DECIMAL(10,2),
    avg_volume BIGINT
);

CREATE TABLE volatility (
    ticker VARCHAR(20),
    volatility DECIMAL(10,6)
);

CREATE TABLE cumulative_comparison (
    ticker VARCHAR(20),
    start_price DECIMAL(10,2),
    end_price DECIMAL(10,2),
    cumulative_return_pct DECIMAL(6,2)
);

CREATE TABLE sector_performance (
    sector VARCHAR(50),
    avg_sector_return_pct DECIMAL(6,2)
);

CREATE TABLE monthly_gainers_losers (
    month VARCHAR(7),
    ticker VARCHAR(20),
    monthly_return_pct DECIMAL(6,2),
    rank_label VARCHAR(10),
    category VARCHAR(10)
);

