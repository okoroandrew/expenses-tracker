from Attributes_of_Expenses_Tracker import *
from Edit_all import *
from screen_clear import clear

print ("==========================================\n")
print ("======  MONTHLY EXPENSES TRACKER  ========\n")
print ("==========================================\n")

while True:
    print ("Select an action")
    print ("1. Add Expenses")
    print ("2. Edit Expenses")
    print ("3. list Expenses")
    print ("4. Get Expenses")
    print ("5. Delete Expenses\n")

    select = input("Select a Number Between 1 and 5: ")
    print ()
    if select == "1":
        print ("Add Expenses")
        Add_expenses()          # a function that allows you record your expenses

    elif select == "2":
        print("1. Edit All")
        print("2. Edit")
        option_ = input("Enter an option: ")
        if option_ == "1":
            Edit_all()
        elif option_ == "2":
            while True:
                print ("Edit Expenses")
                print("1. Edit Title")
                print("2. Edit Amount")
                print("3. Edit Tag")
                print("4. Edit Date")
                print ("0. Quit")
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
        print ("==== List Expenses ====")
        List_expenses()         # a function that reads the txt file and displays the list of expenses

    elif select == "4":
        print ("Get Expenses")
        Get_expenses()

    elif select == "5":
        print ("Delete Expenses")
        print("1. Delete Expenses")
        print("2. Delete ALL Expenses")
        options = input ("SELECT 1 or 2: ")
        if options == "1":
            Delete_expenses()
        elif options == "2":
            warning = input("This will delete all your records: press (y) to continue: ")
            if warning.title() == "Y":
                Delete_all_expenses()

    else:
        print ("Enter a valid command")

    clear()
    stop = input("perform another operation (y/n): ")
    if stop.title() == "N": break
