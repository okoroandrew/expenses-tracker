def Add_expenses():
    """This is a function that adds an item to our list of expenses
    Here you will be prompted to add the expenses: title (String), amount (float)
    tags (List of strings), and date (date)
    """
    #import datetime to convert date string into date object
    from datetime import datetime
    from screen_clear import clear

    clear()
    #Open a txt file to save expenses
    file = open("monthly_expenses_tracker.txt", "a+") #open a text file in a+ mode. a+ is the append and read mode

    while True:
        #Enter title (string) and write to a txt file
        title = input("Enter the Title of the Expenses: ")
        file.write(title)
        file.write(" ")
        clear()
        #Use try except to catch invalid input in amount
        amount = input("Enter the amount spent: ")
        try:
            amount = float(amount)
            file.write(str(amount))
            file.write(" ")
        except:
            print ("Enter a valid number!")

        print ("Select a Tag")
        # select appropriate tag from the list
        tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
        for tag in range (0,5):
            print (tag+1, tags[tag])
        select = input ("Enter number corresponding to tag: ")
        if select == "1":
            tag = "Business/Investment"
        elif select == "2":
            tag = "Welfare"
        elif select == "3":
            tag = "Utilities"
        elif select == "4":
            tag = "Charity"
        else:
            tag = "Other"
        file.write(tag)
        file.write(" ")

        clear()
        #input date as a string, use datetime to convert to a date
        date_string = input("Enter date using the format dd/mm/yy: ")
        try:
            date = datetime.strptime(date_string,"%d/%m/%y") #converts date string to datetime format
            print(date.date())          #The .date() alows you to display just the date instead of date and time
            file.write(str(date.date()))    #allows you to write a string to the text file
        except:
            print ("Enter a valid date!!!")
        file.write("\n")

        clear()

        add_another_expenses = input("Add Another Expenses? y/n")
        if add_another_expenses.title() == "N": break
    file.close()
#add_expenses()


def Edit_expenses_title():
    """This is a function that edits an expenses title. it opens the file in read mode, and uses readlines to read the
    file as a list of strings, line by line. A for loop iterates through each item on the list, use the split method on
    each item to get a list. it uses list slicing, to grab the first item on the list which corresponds to the title. if
    the title corresponds to the title we want to edit, it sets the title to the new title. the join method converts the
    list back to a string, and stored in a new_list. the file is opened in the write mode, and new list is sent to the txt
    file in this mode, which overwrites the content of the file. Thereby, editing the title
    """
    from screen_clear import clear
    clear()

    filehandle = open("monthly_expenses_tracker.txt", "r")
    list_of_expenses = filehandle.readlines()

    title_to_edit = input("Enter Title to edit")
    new_title = input("Enter New Title")
    new_list = []

    for a_list in list_of_expenses:     # iterates through each item in the list_of_expenses
        a_list = a_list.split()         # converts the string to a list using the split method
        if a_list[0] == title_to_edit:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[0] = new_title       # sets the initial title to a new title
        list_to_str = " ".join([str(elem) for elem in a_list])   #uses list comprehension to convert the list to string
        new_list.append(list_to_str + "\n")  #adds the strings to a new list

    filehandle = open("monthly_expenses_tracker.txt", "w") #opens the file in write mode
    filehandle.writelines(new_list)                        # uses writelines method to write new_lines to the file
    filehandle.close()                                     # closes the file

def Edit_expenses_amount():
    """ Edits the amount"""
    from screen_clear import clear
    clear()

    filehandle = open("monthly_expenses_tracker.txt", "r")
    list_of_expenses = filehandle.readlines()

    title_to_edit = input("Enter Title to edit")
    new_amount = input("Enter New Amount")
    new_list = []

    for a_list in list_of_expenses:     # iterates through each item in the list_of_expenses
        a_list = a_list.split()
        if a_list[0] == title_to_edit:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[1] = new_amount
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list.append(list_to_str + "\n")

    filehandle = open("monthly_expenses_tracker.txt", "w") #opens the file in write mode
    filehandle.writelines(new_list)                        # uses writelines method to write new_lines to the file
    filehandle.close()

def Edit_expenses_tag():
    """ Edits the tag"""
    from screen_clear import clear
    clear()

    filehandle = open("monthly_expenses_tracker.txt", "r")
    list_of_expenses = filehandle.readlines()

    title_to_edit = input("Enter Title to edit")
    new_list = []

    # select appropriate tag from the list
    print("Select a Tag")
    tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
    for tag in range(0, 5):
        print(tag+1, tags[tag])

    select = input("Enter number corresponding to tag: ")
    if select == "1":
        tag = "Personal"
    elif select == "2":
        tag = "Business/Investment"
    elif select == "3":
        tag = "Welfare"
    elif select == "4":
        tag = "Utilities"
    elif select == "5":
        tag = "Charity"
    else:
        tag = "Other"

    for a_list in list_of_expenses:     # iterates through each item in the list_of_expenses
        a_list = a_list.split()
        if a_list[0] == title_to_edit:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[2] = tag
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list.append(list_to_str + "\n")

    filehandle = open("monthly_expenses_tracker.txt", "w")  # opens the file in write mode
    filehandle.writelines(new_list)  # uses writelines method to write new_lines to the file
    filehandle.close()

def Edit_expenses_date():
    """ Edits the creation date"""
    from datetime import datetime
    from screen_clear import clear
    clear()

    filehandle = open("monthly_expenses_tracker.txt", "r")
    list_of_expenses = filehandle.readlines()

    title_to_edit = input("Enter Title to edit")
    new_list = []

    date_string = input("Enter date using the format dd/mm/yy: ")
    try:
        date = datetime.strptime(date_string, "%d/%m/%y")  # converts date string to datetime format
        date = date.date()  # The .date() alows you to display just the date instead of date and time
        new_date = str(date)
    except:
        print("Enter a valid date!!!")

    for a_list in list_of_expenses:     # iterates through each item in the list_of_expenses
        a_list = a_list.split()
        if a_list[0] == title_to_edit:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[3] = new_date
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list.append(list_to_str + "\n")

    filehandle = open("monthly_expenses_tracker.txt", "w")  # opens the file in write mode
    filehandle.writelines(new_list)  # uses writelines method to write new_lines to the file
    filehandle.close()


def List_expenses():
    """ A function that reads a text file and displays the list of espenses
    by their title, amount and date_created"""

    #from screen_clear import clear
    #clear
    with open("monthly_expenses_tracker.txt", "r") as filehandle:
        file = filehandle.readlines()
        print ("=============List of Expenses==========")
        for item in file:
            if item == " ":
                print ("No Record Found")
                break
            item = item.split()
            print(f"Title: {item[0].title()}")
            print("Amount: ${}".format(item[1]))
            print("Tag: {}".format(item[2]))
            print(f"Date: {item[3].title()}")
            print("\n")


def Get_expenses():
    """ A function that allows you to search and retrieves expenses using any of the attributes:
    title, amount, tag, date. """

    from datetime import datetime
    with open("monthly_expenses_tracker.txt", "r") as filehandle:
        file = filehandle.readlines()

        print("=========Select Search Option=========")
        print("1. Title")
        print("2. Amount")
        print("3. Tag")
        print("4. Date")

        search_option = input("Enter number corresponding to search option: ")
        if search_option == "1" or search_option == " ":
            search_title = input("Enter Search Title: ")
            for item in file:
                item = item.split()
                if search_title == item[0]:
                    print("Title: {}".format(item[0].title()))
                    print("Amount: ${}".format(item[1]))
                    print("Tag: {}".format(item[2]))
                    print("Date: {}".format(item[3]))
                    print()

        elif search_option == "2":
            search_amount = input("Enter Search Amount: ")
            for item in file:
                item = item.split()
                if search_amount == item[1]:
                    print("Title: {}".format(item[0].title()))
                    print("Amount: ${}".format(item[1]))
                    print("Tag: {}".format(item[2]))
                    print("Date: {}".format(item[3]))
                    print()

        elif search_option == "3":
            search_tag = input("Enter Search Tag: ")
            for item in file:
                item = item.split()
                if search_tag.title() == item[2]:
                    print("Title: {}".format(item[0].title()))
                    print("Amount: ${}".format(item[1]))
                    print("Tag: {}".format(item[2]))
                    print("Date: {}".format(item[3]))
                    print()

        elif search_option == "4":
            date_string = input("Enter date using the format dd/mm/yy: ")
            try:
                date = datetime.strptime(date_string, "%d/%m/%y")  # converts date string to datetime format
                search_date = str(date.date())
                for item in file:
                    item = item.split()
                    if search_date == item[3]:
                        print("Title: {}".format(item[0].title()))
                        print("Amount: ${}".format(item[1]))
                        print("Tag: {}".format(item[2]))
                        print("Date: {}".format(item[3]))
                        print()
            except:
                print("Enter a valid date!!!")
#Get_expenses()


def Delete_expenses():
    """ This is a function that allows you to delete your expenses from the text file.
    The file will be opened in read mode. The readlines is used to read the lines in the file
    and store it in lines.
    The file is then opened again in write mode, for loop is used to go through the variable (lines): line by line,
    lines that does not start with the title of the expense you want to delete are saved in the text file.
    The write mode means that the previous content of the file is over written
    """
    line_to_edit = ''
    with open("monthly_expenses_tracker.txt", "r") as filehandle:
        lines = filehandle.readlines()

    with open("monthly_expenses_tracker.txt", "w") as filehandle:
        item_title = input("Enter the title of expenses to delete: ")
        for line in lines:
            if line.startswith(item_title):
                line_to_edit = line
                continue
            filehandle.write(line)

def Delete_all_expenses():
    """ A function that deletes all expenses from the record
    it writes an empty string to the file"""

    empty = " "
    with open("monthly_expenses_tracker.txt", "w") as filehandle:
        filehandle.write(empty)



