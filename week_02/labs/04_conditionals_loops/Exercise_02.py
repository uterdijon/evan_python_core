'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''
*********************
number = int(input("Enter a number from 1 to 7:"))
if number == 1:
    print("The day is Monday.")
else:
    if number == 2:
        print("The day is Tuesday.")
    else:
        if number == 3:
            print("The day is Wednesday.")
        else:
            if number == 4:
                print("The day is Thursday.")
            else:
                if number == 5:
                    print("The day is Friday.")
                else:
                    if number == 6:
                        print("The day is Saturday.")
                    else:
                        print("The day is Sunday.")
*********************
