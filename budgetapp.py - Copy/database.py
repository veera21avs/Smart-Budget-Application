import sqlite3

conn = sqlite3.connect("budget.db")

cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    email TEXT,
    username TEXT,
    password TEXT
)
""")

# Budget Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS budgets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_amount REAL,
    daily_budget REAL
)
""")

# Expenses Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_name TEXT,
    amount REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")