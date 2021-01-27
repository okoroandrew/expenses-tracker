# The screen clear function
def clear():
    import os
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')

    # for windows platform
    else:
        _ = os.system('cls')