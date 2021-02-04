from expenses_tracker_table import *
from datetime import datetime
from screen_clear import clear
import sqlite3

def Add_expenses():
    """This is a function that adds an item to our list of expenses
    Here you will be prompted to add the expenses: title (String), amount (float)
    tags (List of strings), and date (date)
    """
    clear()
    data_list = []
    while True:
        title = input("Enter the Title of the Expenses: ")
        clear()
        # Use try except to catch invalid input in amount
        while True:
            amount = input("Enter the amount spent: ")
            try:
                amount = float(amount)
                break
            except:
                print("Enter a valid number!")

        print("Select a Tag")
        # select appropriate tag from the list
        while True:
            tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
            for tag in range(0, 5):
                print(tag + 1, tags[tag])
            select = input("Enter number corresponding to tag: ")
            if select == "2":
                clear()
                tag = "Business/Investment"
                break
            elif select == "3":
                clear()
                tag = "Welfare"
                break
            elif select == "4":
                clear()
                tag = "Utilities"
                break
            elif select == "5":
                clear()
                tag = "Charity"
                break
            elif select == "1":
                clear()
                tag = "Personal"
                break
            else:
                clear()
                print("Select a valid number")
                continue

        # input date as a string, use datetime to convert to a date
        while True:
            clear()
            date_string = input("Enter date using the format dd/mm/yy: ")
            try:
                date = datetime.strptime(date_string, "%d/%m/%y")  # converts date string to datetime format
                date = date.date()  # The .date() alows you to display just the date instead of date and time
                break
            except:
                print("Enter a valid date!!!")

        data = (title, amount, tag, date)
        data_list.append(data)

        clear()
        add_another_expenses = input("Add Another Expenses? y/n")
        if add_another_expenses.title() == "N": break
    insert_into_table(data_list)



def Edit_all():
    """ Edits the whole row"""
    clear()
    new_title = input("Enter new title: ")
    while True:
        try:
            new_amount = float(input("Enter new amount: "))
            break
        except:
            print("Enter a valid amount")
    tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
    print("=======TAGS=======")
    print("1. Personal")
    print("2. Business/Investment")
    print("3. Welfare")
    print("4. Utilities")
    print("5. Charity")

    while True:
        options = input("Select Tag : ")
        if options == "1":
            new_tag = tags[0]
            break
        elif options == "2":
            new_tag = tags[1]
            break
        elif options == "3":
            new_tag = tags[2]
            break
        elif options == "4":
            new_tag = tags[3]
            break
        elif options == "5":
            new_tag = tags[4]
            break
        else:
            print("select a valid tag")

    while True:
        try:
            date_string = input("Enter new date dd/mm/yy: ")
            date = datetime.strptime(date_string, "%d/%m/%y")
            new_date = date.date()
            break
        except:
            print("Enter a valid date")

    while True:
        try:
            id = int(input("enter the Id: "))
            break
        except:
            print("enter a valid id")
    try:
        conn = sqlite3.connect("monthly_expenses_tracker.db")
        cur = conn.cursor()
        sqlite_update_query = """UPDATE Expenses_Tracker SET title= ?, amount =?,
                                tag = ?, created_at = ? WHERE id = ?""";
        cur.execute(sqlite_update_query, (new_title, new_amount, new_tag, new_date, id))
        conn.commit()
    except:
        print("Failed")
    finally:
        if conn:
            conn.close()
#Edit_all()

def Edit_expenses_title():
    """This is a function that edits an expenses title.
    It does it by using the Update querry, setting the old title to a new title"""
    clear()
    new_title = input("Enter new title: ")
    while True:
        try:
            id = int(input("enter the Id: "))
            break
        except:
            print("Enter a valid id")
    try:
        conn = sqlite3.connect("monthly_expenses_tracker.db")
        cur = conn.cursor()
        sqlite_update_query = """UPDATE Expenses_Tracker SET title = ?
                                WHERE id = ?""";

        cur.execute(sqlite_update_query,(new_title, id))
        conn.commit()
        cur.close()
    except:
        print("Failed to connect and update db")
    finally:
        if conn:
            conn.close()

#Edit_expenses_title()


def Edit_expenses_amount():
    """ Edits the amount"""
    clear()
    try:
        conn = sqlite3.connect("monthly_expenses_tracker.db")
        cur = conn.cursor()
        sqlite_update_amount_query = """UPDATE Expenses_Tracker SET amount = ?
                                        WHERE id = ?""";
        while True:
            try:
                new_amount = float(input("Enter new amount: "))
                break
            except:
                print("enter a valid amount")
        while True:
            try:
                id = int(input("Enter id: "))
                break
            except:
                print("enter a valid id")

        cur.execute(sqlite_update_amount_query, (new_amount, id))
        conn.commit()
        cur.close()
    except:
        print("failed to connect and update")
    finally:
        if conn:
            conn.commit()
#Edit_expenses_amount()


def Edit_expenses_tag():
    """ Edits the tag"""
    clear()
    tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
    print("=======TAGS=======")
    print("1. Personal")
    print("2. Business/Investment")
    print("3. Welfare")
    print("4. Utilities")
    print("5. Charity")

    while True:
        options = input("Select Tag : ")
        if options == "1":
            new_tag = tags[0]
            break
        elif options == "2":
            new_tag = tags[1]
            break
        elif options == "3":
            new_tag = tags[2]
            break
        elif options == "4":
            new_tag = tags[3]
            break
        elif options == "5":
            new_tag = tags[4]
            break
        else:
            print("Enter a valid number")

    while True:
        try:
            id = int(input("enter the Id: "))
            break
        except:
            print("enter a valid id")

    try:
        conn = sqlite3.connect("monthly_expenses_tracker.db")
        cur = conn.cursor()
        sqlite_update_query = """UPDATE Expenses_Tracker SET tag = ?
                                    WHERE id = ?""";

        cur.execute(sqlite_update_query, (new_tag, id))
        conn.commit()
    except:
        print("Failed")
    finally:
        if conn:
            conn.close()
#Edit_expenses_tag()

def Edit_expenses_date():
    """ Edits the creation date"""
    clear()
    try:
        conn = sqlite3.connect("monthly_expenses_tracker.db")
        cur = conn.cursor()
        sqlite_update_amount_query = """UPDATE Expenses_Tracker SET created_at = ?
                                        WHERE id = ?""";
        while True:
            try:
                date_string = input("Enter new date dd/yy/mm: ")
                date = datetime.strptime(date_string, "%d/%m/%y")
                new_date = date.date()
                break
            except:
                print("Enter a valid date")

        while True:
            try:
                id = int(input("Enter id: "))
                break
            except:
                print("Enter a valid id")
                
        cur.execute(sqlite_update_amount_query, (new_date, id))
        conn.commit()
        cur.close()

    except:
        print("failed to connect and update")
    finally:
        if conn:
            conn.commit()
#Edit_expenses_date()

def List_expenses():
    """ A function that displays the list of espenses contained in the database
    by their title, amount and date_created"""
    try:
        connection = sqlite3.connect("monthly_expenses_tracker.db")
        cursor = connection.cursor()
        sqlite_select_all_query = "SELECT * FROM Expenses_Tracker"
        for row in cursor.execute(sqlite_select_all_query):
            print(f"{row[0]}. Title: {row[1]}")
            print("Amount: ${}".format(row[2]))
            print("Tag: {}".format(row[3]))
            print(f"Date: {row[4]} \n")

        cursor.close()
    except sqlite3.Error:
        print("Failed to Retrieve List")
    finally:
        if connection:
            connection.close()

#List_expenses()


def Get_expenses():
    """ A function that allows you to search and retrieves expenses using any of the attributes:
    title, amount, tag, date. """

    try:
        connection = sqlite3.connect("monthly_expenses_tracker.db")
        cursor = connection.cursor()
        sqlite_get_expenses_query = "SELECT * FROM Expenses_Tracker"

        print("=========Select Search Option=========")
        print("1. Title")
        print("2. Amount")
        print("3. Tag")
        print("4. Date")
        while True:
            try:
                search_option = int(input("Enter Search option: "))
                if search_option == 1:
                    clear()
                    search_title = input("Enter Search Title: ")
                    for row in cursor.execute(sqlite_get_expenses_query):
                        if search_title == row[1]:
                            print("Title: {}".format(row[1].title()))
                            print("Amount: ${}".format(row[2]))
                            print("Tag: {}".format(row[3]))
                            print("Date: {}".format(row[4]))
                            print()
                    break

                elif search_option == 2:
                    clear()
                    while True:
                        try:
                            search_amount = float(input("Enter Search Amount: "))
                            break
                        except:
                            print("Enter a valid amount")
                    for row in cursor.execute(sqlite_get_expenses_query):
                        if search_amount == row[2]:
                            print("Title: {}".format(row[1].title()))
                            print("Amount: ${}".format(row[2]))
                            print("Tag: {}".format(row[3]))
                            print("Date: {}".format(row[4]))
                            print()
                    break

                elif search_option == 3:
                    clear()
                    search_tag = input("Enter Search Tag: ")
                    for row in cursor.execute(sqlite_get_expenses_query):
                        if search_tag == row[3]:
                            print("Title: {}".format(row[1].title()))
                            print("Amount: ${}".format(row[2]))
                            print("Tag: {}".format(row[3]))
                            print("Date: {}".format(row[4]))
                            print()
                    break

                elif search_option == 4:
                    clear()
                    while True:
                        try:
                            search_date = input("Enter Search date dd/mm/yy: ")
                            date = datetime.strptime(search_date, "%d/%m/%y")
                            search_date2 = date.date()
                            break
                        except:
                            print("enter a valid date")

                    for row in cursor.execute(sqlite_get_expenses_query):
                        if search_date2 == row[4]:
                            print("Title: {}".format(row[1].title()))
                            print("Amount: ${}".format(row[2]))
                            print("Tag: {}".format(row[3]))
                            print("Date: {}".format(row[4]))
                            print()
                    break

                else:
                    print("Select a valid number")
                    continue
            except:
                print("Enter a valid number")
    except sqlite3.Error:
        print("Failed to connect!!!")
    finally:
        if connection:
            connection.close()

#Get_expenses()


def Delete_expenses():
    """ This is a function that allows you to delete your expenses from the database using their title.
    it prompts you to enter the title of the expenses you want to delete, and deletes it.
    if there are more than one expenses with the same title, it displays them and prompts you to enter
    the id of the one you want to delete.
    """
    try:
        connection = sqlite3.connect("monthly_expenses_tracker.db")
        cursor = connection.cursor()
        sqlite_delete_query = """DELETE FROM Expenses_Tracker
                                WHERE title = ?"""
        title_of_row_to_delete = input("Enter title of Expenses to delete: ")
        cursor.execute(sqlite_delete_query,(title_of_row_to_delete, ))
        connection.commit()
        cursor.close()

    except sqlite3.Error:
        print("Failed to delete all !!!")

    finally:
        if connection:
            connection.close()
#Delete_expenses()

def Delete_all_expenses():
    """ A function that deletes all expenses from the record
    """
    try:
        connection = sqlite3.connect("monthly_expenses_tracker.db")
        cursor = connection.cursor()
        sqlite_delete_all_query = "DELETE FROM Expenses_Tracker"
        cursor.execute(sqlite_delete_all_query)
        #connection.commit()                    i commented it out for test sake,
        cursor.close()

    except sqlite3.Error:
        print("Failed to delete all !!!")

    finally:
        if connection:
            connection.close()

#Delete_all_expenses()