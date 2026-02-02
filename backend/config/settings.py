from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # ClickHouse
    clickhouse_host: str = "localhost"
    clickhouse_port: int = 9000
    clickhouse_database: str = "crypto_market"

    # Binance
    binance_ws_url: str = "wss://stream.binance.com:9443/ws"
    binance_symbols: List[str] = ["btcusdt", "ethusdt", "solusdt"]
    binance_reconnect_delay: int = 5  # seconds
    binance_max_reconnect_attempts: int = 5

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_cors_origins: List[str] = ["http://localhost:3000"]

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
