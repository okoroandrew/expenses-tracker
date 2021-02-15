from screen_clear import *
from datetime import datetime
from expenses_tracker_table import *


class Expense(object):
    """
    An expenses class with attributes like title(string), amount(float), created_at (date)
    and tags (list of strings)
    """
    def __init__(self, title=None, amount=None, created_at=None, tag=None):
        """initializes the attributes"""
        self.title = title
        self.amount = amount
        self.created_at = created_at
        self.tag = tag


class ExpenseRepository(Expense):
    """ A class that allows you perform operations like save, get_by_id, list
    and delete"""

    def add_expense_title(self):
        """takes input for title, amount, created_at, tag
        """
        self.title = input("Enter the Title of the Expenses: ")
        return self.title

    def add_expense_amount(self):
        clear()
        # Use try except to catch invalid input in amount
        while True:
            self.amount = input("Enter the amount spent: ")
            try:
                self.amount = float(self.amount)
                return self.amount
                break
            except:
                print("Enter a valid number!")

    def add_expense_tag(self):
        print("Select a Tag")
        # select appropriate tag from the list
        while True:
            tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
            for tag in range(0, 5):
                print(tag + 1, tags[tag])
            select = input("Enter number corresponding to tag: ")
            if select == "2":
                clear()
                self.tag = "Business/Investment"
                return self.tag
                break
            elif select == "3":
                clear()
                self.tag = "Welfare"
                return self.tag
                break
            elif select == "4":
                clear()
                self.tag = "Utilities"
                return self.tag
                break
            elif select == "5":
                clear()
                self.tag = "Charity"
                return self.tag
                break
            elif select == "1":
                clear()
                self.tag = "Personal"
                return self.tag
                break
            else:
                clear()
                print("Select a valid number")
                continue

    def add_expense_created_at(self):
        # input date as a string, use datetime to convert to a date
        while True:
            clear()
            date_string = input("Enter date using the format dd/mm/yy: ")
            try:
                date = datetime.strptime(date_string, "%d/%m/%y")  # converts date string to datetime format
                self.created_at = date.date() # The .date() alows you to display just the date instead of date and time
                return self.created_at
                break
            except:
                print("Enter a valid date!!!")

    def save_to_db(self):
        """A method that saves the expense attributes to the db
        """
        data_tuple = (self.title, self.amount, self.tag, self.created_at)
        insert_into_table(data_tuple)

    def list_expense(self):
        """ A function that displays the list of expenses contained in the database
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

    def get_by_id(self):
        """
        #############
        """
        try:
            connection = sqlite3.connect("monthly_expenses_tracker.db")
            cursor = connection.cursor()
            sqlite_get_expenses_query = "SELECT * FROM Expenses_Tracker"
            search_id = int(input("Enter Search Id: "))
            for row in cursor.execute(sqlite_get_expenses_query):
                if search_id == row[0]:
                    print("Title: {}".format(row[1].title()))
                    print("Amount: ${}".format(row[2]))
                    print("Tag: {}".format(row[3]))
                    print("Date: {}".format(row[4]))
                    print()

        except sqlite3.Error:
            print("Failed to connect!!!")
        finally:
            if connection:
                connection.close()

    def delete_all_expenses(self):
        """ A method that deletes all expenses from the record
        """
        try:
            connection = sqlite3.connect("monthly_expenses_tracker.db")
            cursor = connection.cursor()
            sqlite_delete_all_query = "DELETE FROM Expenses_Tracker"
            cursor.execute(sqlite_delete_all_query)
            # connection.commit()                    i commented it out for test sake,
            cursor.close()

        except sqlite3.Error:
            print("Failed to delete all !!!")

        finally:
            if connection:
                connection.close()

    def delete_expense(self):
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
            cursor.execute(sqlite_delete_query, (title_of_row_to_delete,))
            connection.commit()
            cursor.close()

        except sqlite3.Error:
            print("Failed to delete all !!!")

        finally:
            if connection:
                connection.close()


testi = ExpenseRepository()
testi.delete_expense()