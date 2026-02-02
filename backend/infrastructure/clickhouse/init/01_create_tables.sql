-- Create database
CREATE DATABASE IF NOT EXISTS crypto_market;

-- Price ticks table
CREATE TABLE IF NOT EXISTS crypto_market.price_ticks
(
    symbol String,
    price Decimal64(8),
    timestamp DateTime64(6, 'UTC'),
    source String DEFAULT 'binance'
)
ENGINE = MergeTree()
ORDER BY (symbol, timestamp)
PARTITION BY toYYYYMMDD(timestamp)
TTL timestamp + INTERVAL 24 HOUR;

-- OHLC bars table
-- Order book snapshots table