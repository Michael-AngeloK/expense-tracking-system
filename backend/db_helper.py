import os
from pathlib import Path
from dotenv import load_dotenv
import mysql.connector
from contextlib import contextmanager

# Load .env from folder
env_path = Path("envs") / ".env"
load_dotenv(dotenv_path=env_path)

# Access vars
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

if not USER or not PASSWORD:
    raise ValueError("Missing environment variables")


def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = USER,
        password = PASSWORD,
        database="expense_manager"
    )
