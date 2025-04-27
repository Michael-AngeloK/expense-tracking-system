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

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = USER,
        password = PASSWORD,
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_all_records():
    query = "SELECT * from expenses"
    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", [expense_date])
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            [expense_date, amount, category, notes]
        )

def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", [expense_date])

if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-08-01")
    # print(expenses)
    # insert_expense("2025-04-26", 40, "Food", "Spicy Food")
    # delete_expenses_for_date("2025-04-26")
    pass