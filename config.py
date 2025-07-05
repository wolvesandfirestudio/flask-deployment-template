# config.py
import os

class Config:
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "your_jwt_secret_key_here")
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024  # 25 MB

    # Optional file storage config
    DATA_DIR = "data"
    LOG_FILE = "log.txt"

    # Optional third-party API keys
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
    STRIPE_PRICE_ID = os.environ.get("STRIPE_PRICE_ID")