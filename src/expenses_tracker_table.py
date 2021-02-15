import sqlite3


def create_table():
    """ A program for creating a sqlite table to storing expenses in db.
     the table has roles: id, title, Amount, tag, creation_date"""

    try:
        connection = sqlite3.connect("monthly_expenses_tracker_class.db")
        cursor = connection.cursor()
        sqlite3_create_table_query = """CREATE TABLE Expenses_Tracker (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            amount REAL NOT NULL,
                            tag TEXT); """
        cursor.execute(sqlite3_create_table_query)
        print("table successfully created")
        cursor.close()
    except sqlite3.Error:
        print("Error occurred while creating table.")
    finally:
        if connection:
            connection.close()


def insert_into_table(data_list):
    """A program that inserts values into the table
    """

    try:
        connection = sqlite3.connect("monthly_expenses_tracker.db")
        cursor = connection.cursor()
        sqlite3_insert_table_query = """ INSERT INTO Expenses_Tracker
                                    (title, amount, tag, created_at) VALUES
                                    (?,?,?,?);"""
        data_tuple = data_list
        cursor.execute(sqlite3_insert_table_query, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error:
        print("Error Occurred While Inserting Into Table")

    finally:
        if connection:
            connection.close()

