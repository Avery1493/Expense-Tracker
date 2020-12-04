import sqlite3
from sqlite3 import Error


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


def main():
    database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"

    sql_create_expense_table = """ CREATE TABLE IF NOT EXISTS expenses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        amount float,
        created_at text,
        tags text
    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_expense_table)
    else:
        print("Error! Cannot create the database connection")


if __name__ == "__main__":
    main()
