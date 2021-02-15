from expenses_attributes import *
from Attributes_of_Expenses_Tracker import *
from screen_clear import clear

print("==========================================\n")
print("======  MONTHLY EXPENSES TRACKER  ========\n")
print("==========================================\n")

expense = ExpenseRepository()       # instance of the class
while True:
    print("Select an action")
    print("1. Add Expenses")
    print("2. Edit Expenses")
    print("3. list Expenses")
    print("4. Get Expenses")
    print("5. Delete Expenses\n")

    select = input("Select a Number Between 1 and 5: ")
    print()
    if select == "1":
        clear()
        print("Add Expenses")
        expense.add_expense_title()
        expense.add_expense_amount()
        expense.add_expense_tag()
        expense.add_expense_created_at()
        expense.save_to_db()

    elif select == "2":
        clear()
        print("1. Edit All")
        print("2. Edit")
        option_ = input("Enter an option: ")
        if option_ == "1":
            Edit_all()
        elif option_ == "2":
            while True:
                print("Edit Expenses")
                print("1. Edit Title")
                print("2. Edit Amount")
                print("3. Edit Tag")
                print("4. Edit Date")
                print("0. Quit")
                option = input("Select 1-4: ")
                if option == "1":
                    Edit_expenses_title()
                elif option == "2":
                    Edit_expenses_amount()
                elif option == "3":
                    Edit_expenses_tag()
                elif option == "4":
                    Edit_expenses_date()
                elif option == "0":
                    break

    elif select == "3":
        clear()
        print("==== List Expenses ====")
        expense.list_expense()  # a function that reads the txt file and displays the list of expenses

    elif select == "4":
        clear()
        print("Get Expenses")
        expense.get_by_id()

    elif select == "5":
        clear()
        print("Delete Expenses")
        print("1. Delete Expenses")
        print("2. Delete ALL Expenses")
        options = input("SELECT 1 or 2: ")
        if options == "1":
            clear()
            expense.delete_expense()
        elif options == "2":
            clear()
            warning = input("This will delete all your records: press (y) to continue: ")
            if warning.title() == "Y":
                clear()
                expense.delete_all_expenses()

    else:
        clear()
        print("Enter a valid command")
        continue

    clear()
    stop = input("perform another operation (y/n): ")
    if stop.title() == "N":
        break
