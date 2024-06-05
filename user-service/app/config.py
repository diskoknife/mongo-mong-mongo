import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file (if exists)

class Config:
    # General Config
    DEBUG = os.environ.get("DEBUG", False)  # Set to True for development mode
    TESTING = False  # Set to True for testing mode
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # MongoDB Config
    DB_URL = os.environ.get("DB_URL", "mongodb://localhost:27017")  # Default to localhost
    DB_NAME = os.environ.get("DB_NAME", "your_database_name")

    # Other Config (e.g., JWT, logging, etc.)
    # ... add as needed
    # Redis Config
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
    REDIS_DB = os.environ.get("REDIS_DB", 0)

    # JWT Config
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600)  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = os.environ.get("JWT_REFRESH_TOKEN_EXPIRES", 2592000)  # 30 days

    # Logging Config
    LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "INFO")
    LOGGING_FORMAT = os.environ.get("LOGGING_FORMAT", "%(asctime)s - %(levelname)s - %(message)s")

    # Email Config
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = os.environ.get("EMAIL_PORT")
    EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
    EMAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    EMAIL_SENDER = os.environ.get("EMAIL_SENDER")

    # Other Config (e.g., API keys, etc.)
    # ... add as needed
    
