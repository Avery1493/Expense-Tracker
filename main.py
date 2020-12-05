
# Readlines
def read_lines():
    '''Opens and reads expense.txt file and prints each line.'''
    file_1 = open("expense.txt", "r")
    Lines = file_1.readlines()
    for line in Lines:
        print(line)


# Add Expense (append)
def add_expense(new_expense):
    '''Takes in a new expense as a parameter.
    Adds expense as a new line to expense.txt file.
    Returns last line in file.'''
    file_1 = open("expense.txt", "a")
    file_1.write(new_expense)
    file_1 = open("expense.txt", "r")
    Lines = file_1.readlines()
    return Lines[-1]


# List Expenses
def list_expenses():
    '''Opens expense.txt file and skips header row.
    Prints the title attribute of each line'''
    file_1 = open("expense.txt", "r")
    next(file_1)
    Lines = file_1.readlines()
    for line in Lines:
        print(line.split(",")[0])


# Get Expense
def get_expense(index):
    '''Takes in index of expense -starting a zero excluding header.
    Returns expense at index.'''
    file_1 = open("expense.txt", "r")
    next(file_1)
    Lines = file_1.readlines()
    return Lines[int(index)]


# Edit Expense
def edit_expense(index, string):
    '''
    Takes in index of expense line to be edited. 
    Replaces line with string and overrides file.
    '''
    # get expense
    edit_line = str(get_expense(index))
    with open("expense.txt", "r") as file_1:
        Lines = file_1.readlines()
        # edit expense
        Lines[index + 1] = Lines[index + 1].replace(edit_line, string)
        # write new file / override existing file
        with open("expense.txt", "w") as file_2:
            for line in Lines:
                file_2.write(line)


# Delete Expense
def delete_expense(index):
    '''Takes in index of expense. 
    Gets and removes line. Overrides
    file with updated expenses.'''
    # get expense
    delete_line = str(get_expense(index))
    with open("expense.txt", "r") as file_1:
        Lines = file_1.readlines()
        # remove expense
        Lines.remove(delete_line)
        # write new file / override existing file
        with open("expense.txt", "w") as file_2:
            for line in Lines:
                file_2.write(line)


if __name__ == "__main__":
    print("---READ LINES---")
    read_lines()

    print("---ADD EXPENSE---")
    new_expense = '\n"walmart",18.69,"12/06/2020","shopping"'
    new_expense_2 = '\n"walmart",7.84,"12/07/2020","shopping"'
    print(add_expense(new_expense))
    print(add_expense(new_expense_2))

    print("---LIST EXPENSES---")
    list_expenses()

    print("---GET EXPENSE---")
    print(get_expense(10))

    print("---EDIT EXPENSE---")
    string = '"walmart",7.64,"12/06/2020","shopping"'
    edit_expense(10, string)

    print("---DELETE EXPENSE---")
    delete_expense(10)
    delete_expense(9)
