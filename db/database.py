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


def create_expense(conn, expense):
    sql = ''' INSERT INTO expenses(title,amount,created_at,tags)
        VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, expense)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"

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
        expense = ("walmart", 18.69, "12/06/2020", '["shopping"]')
        create_expense(conn, expense)


if __name__ == "__main__":
    main()
