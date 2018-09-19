'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
def ask_for_int():
    try:
        var = input("Please enter an integer: ")
        assert (type(var) == int), "That is not an integer!"
    except AssertionError as notint:
        print(notint)
        ask_for_int()


    else:
        print("That is an integer.")

ask_for_int()
