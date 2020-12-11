import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()


class Expense():
    def __init__(self, title, amount, created_at, tags):
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = created_at
        self.tags = tags

    def __repr__(self):
        return "{self.__class__.__name__}({self.title}, {self.amount}, {self.created_at}, {self.tags})".format(self=self)

    def __str__(self):
        return "Title: {self.title}, Amount:  {self.amount}, Created_At:  {self.created_at}, Tags: {self.tags}".format(self=self)


class ExpenseRepository():

    def CreateTable():
        database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        query = ''' CREATE TABLE IF NOT EXISTS expenses(
        id integer PRIMARY KEY,
        title text NOT NULL,
        amount real,
        created_at text,
        tags text);'''
        conn.commit()
        conn.close()
        return None

    def AddExpense(expense):
        database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        query = ''' INSERT INTO expenses(title,amount,created_at,tags)
        VALUES(?,?,?,?)'''

        cursor.execute(query, [str(expense.title), expense.amount,
                               str(expense.created_at), str(expense.tags)])
        conn.commit()
        conn.close()
        return None

    def EditExpense(expense, id):
        database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        query = ''' UPDATE expenses
        SET "title" = ?, "amount" = ?, "created_at" = ?, "tags" = ?
        wHERE "id" = ?'''

        cursor.execute(query, [str(expense.title), expense.amount,
                               str(expense.created_at), str(expense.tags), (id)])
        conn.commit()
        conn.close()
        return None

    def GetById(id):
        database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        query = ''' SELECT *
        FROM expenses
        wHERE "id" = ?'''

        cursor.execute(query, (id,))
        row = cursor.fetchall()
        conn.close()
        return row

    def ListAll():
        database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        query = ''' SELECT *
        FROM expenses'''

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def Delete(id):
        database = r"C:\Users\avery\Lambda\Expense-Tracker\db\exp.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        query = '''DELETE FROM expenses WHERE "id"= ?'''

        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return None


if __name__ == "__main__":
    exp = Expense("target", 45, "12/06/20", ["shopping", "bills"])
    exp2 = Expense("walmart", 43.78, "12/07/20", ["shopping", "bills", "food"])
    print(exp)
    print(exp.__str__())
    print(exp.__repr__())

    print("Title:", exp.title)
    print("Amount:", exp.amount)
    print("Created_On:", exp.created_at)
    print("Tags:", exp.tags)

    er = ExpenseRepository
    er.AddExpense(exp)
    er.AddExpense(exp)
    er.EditExpense(exp2, 10)
    print(er.GetById(10))
    print(er.ListAll())
    er.Delete(11)
    er.Delete(10)
