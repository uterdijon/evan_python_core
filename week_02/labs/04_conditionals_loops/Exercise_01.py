'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''
*******************
print("This program determines whether a number is even or odd.")
number = int(input("Enter a number between 1 and 1,000,000,000:"))
if number % 2 == 0:
    print("This number is even.")
else: 
    print("This number is odd.")
*******************
