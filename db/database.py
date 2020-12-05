import sqlite3
from sqlite3 import Error
import pandas as pd

# Database
database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_expense(conn, expense):
    sql = ''' INSERT INTO expenses(title,amount,created_at,tags)
        VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, expense)
    conn.commit()
    return cur.lastrowid


def main():
    sql_create_expense_table = """ CREATE TABLE IF NOT EXISTS expenses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        amount real,
        created_at text,
        tags text
    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_expense_table)
    else:
        print("Error! Cannot create the database connection")

    with conn:
        expense = ("geico", 90.65, "11/24/2020",
                   "vehicle, insurance, bills")
        create_expense(conn, expense)

    conn.close


def body(file_path):
    # Convert txt to csv
    read_file = pd.read_csv(file_path)

    # Save csv
    read_file.to_csv(
        r"C:\Users\avery\Lambda\Expense-Tracker\exp.csv", index=False)

    # Load csv
    expenses = pd.read_csv(r"C:\Users\avery\Lambda\Expense-Tracker\exp.csv")

    # Connect to database
    conn = create_connection(database)

    # Copy csv to database
    if conn is not None:
        expenses.to_sql('expenses', conn, if_exists='append', index=False)
    else:
        print("Error! Cannot create the database connection")


if __name__ == "__main__":
    main()
    body(r"C:\Users\avery\Lambda\Expense-Tracker\expense.TXT")
