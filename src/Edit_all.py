def Edit_all():
    """This is a function that edits an expenses title. it opens the file in read mode, and uses readlines to read the
    file as a list of strings, line by line. A for loop iterates through each item on the list, use the split method on
    each item to get a list. it uses list slicing, to grab the first item on the list which corresponds to the title. if
    the title corresponds to the title we want to edit, it sets the title to the new title. the join method converts the
    list back to a string, and stored in a new_list. the file is opened in the write mode, and new list is sent to the txt
    file in this mode, which overwrites the content of the file. Thereby, editing the title. Same applies to amount, tag
    and date
    """
    from datetime import datetime
    from screen_clear import clear
    clear()

    filehandle = open("monthly_expenses_tracker.txt", "r")
    list_of_expenses = filehandle.readlines()

    title_to_edit = input("Enter Title to edit")
    new_title = input("Enter New Title")
    new_list1 = []
    new_list2 = []
    new_list3 = []
    new_list4 = []

    for a_list in list_of_expenses:  # iterates through each item in the list_of_expenses
        a_list = a_list.split()  # converts the string to a list using the split method
        if a_list[0] == title_to_edit:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[0] = new_title  # sets the initial title to a new title
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list1.append(list_to_str + "\n")  # adds the strings to a new list

    new_amount = input("Enter New Amount")

    for a_list in new_list1:  # iterates through each item in the list_of_expenses
        a_list = a_list.split()
        if a_list[0] == new_title:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[1] = new_amount
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list2.append(list_to_str + "\n")

    # select appropriate tag from the list
    print("Select a Tag")
    tags = ["Personal", "Business/Investment", "Welfare", "Utilities", "Charity"]
    for tag in range(0, 5):
        print(tag + 1, tags[tag])

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

    for a_list in new_list2:  # iterates through each item in the list_of_expenses
        a_list = a_list.split()
        if a_list[0] == new_title:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[2] = tag
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list3.append(list_to_str + "\n")

    date_string = input("Enter date using the format dd/mm/yy: ")
    try:
        date = datetime.strptime(date_string, "%d/%m/%y")  # converts date string to datetime format
        date = date.date()  # The .date() alows you to display just the date instead of date and time
        new_date = str(date)
    except:
        print("Enter a valid date!!!")

    for a_list in new_list3:  # iterates through each item in the list_of_expenses
        a_list = a_list.split()
        if a_list[0] == new_title:  # checks if the first item of each iteration corresponds to the title_to_edit
            a_list[3] = new_date
        list_to_str = " ".join([str(elem) for elem in a_list])  # uses list comprehension to convert the list to string
        new_list4.append(list_to_str + "\n")

    filehandle = open("monthly_expenses_tracker.txt", "w")  # opens the file in write mode
    filehandle.writelines(new_list4)  # uses writelines method to write new_lines to the file
    filehandle.close()

