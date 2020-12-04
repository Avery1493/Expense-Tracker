
# Readlines
def read_lines():
    file_1 = open("expense.txt", "r")
    Lines = file_1.readlines()
    for line in Lines:
        print(line)


# Add Expense (append)
def add_expense(new_expense):
    file_1 = open("expense.txt", "a")
    file_1.write(new_expense)
    file_1 = open("expense.txt", "r")
    Lines = file_1.readlines()
    return Lines[-1]


# List Expenses
def list_expenses():
    file_1 = open("expense.txt", "r")
    next(file_1)
    Lines = file_1.readlines()
    for line in Lines:
        print(line.split(",")[0])


# Get Expense
def get_expense(index):
    file_1 = open("expense.txt", "r")
    next(file_1)
    Lines = file_1.readlines()
    return Lines[int(index)]


# Edit Expense
def edit_expense(int, string):
    # get expense
    edit_line = str(get_expense(int))
    with open("expense.txt", "r") as file_1:
        Lines = file_1.readlines()
        # edit expense
        Lines[int + 1] = Lines[int + 1].replace(edit_line, string)
        # write new file / override existing file
        with open("expense.txt", "w") as file_2:
            for line in Lines:
                file_2.write(line)
    # edit_line = edit_line.replace(edit_line, string)


# Delete Expense
def delete_expense(int):
    # get expense
    delete_line = str(get_expense(int))
    with open("expense.txt", "r") as file_1:
        Lines = file_1.readlines()
        # remove expense
        Lines.remove(delete_line)
        # write new file / override existing file
        with open("expense.txt", "w") as file_2:
            for line in Lines:
                file_2.write(line)


if __name__ == "__main__":
    print("READ LINES")
    read_lines()

    print("ADD EXPENSE")
    new_expense = '\n"walmart",18.69,"12/06/2020","shopping"'
    new_expense_2 = '\n"walmart",7.84,"12/07/2020","shopping"'
    print(add_expense(new_expense))
    print(add_expense(new_expense_2))

    print("LIST EXPENSES")
    list_expenses()

    print("GET EXPENSE")
    print(get_expense(10))

    print("EDIT EXPENSE")
    string = '"walmart",7.64,"12/06/2020","shopping"'
    edit_expense(10, string)

    print("DELETE EXPENSE")
    delete_expense(9)
