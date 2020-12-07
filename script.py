import sqlite3


def main(database, txt_file):
    '''Copies all existing expenses from TXT file to a database.'''
    # load file, skip header
    file = open(txt_file, "r")
    next(file)
    lines = file.readlines()

    # connect to data base
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # create table if not exists
    query = '''CREATE TABLE IF NOT EXISTS expenses (
            id integer PRIMARY KEY,
            title text NOT NULL,
            amount real,
            created_at text,
            tags text);'''

    cursor.execute(query)

    # copy file to database
    for line in lines:
        a = line.split(",")[0]
        b = line.split(",")[1]
        c = line.split(",")[2]
        d = line.split(",")[3::]
        query2 = '''INSERT INTO expenses(title, amount, created_at, tags)
            VALUES (?,?,?,?);'''
        cursor.execute(query2, (a, b, c, str(d)))
        conn.commit()

    conn.close()


if __name__ == "__main__":
    database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
    txt_file = "expense.txt"

    main(database, txt_file)
