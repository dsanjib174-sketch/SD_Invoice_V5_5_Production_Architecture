import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    APP_NAME = "SMART DADA SOLUTION"
    APP_VERSION = "V5.5"
