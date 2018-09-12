'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''
************************
lower = int(input("Enter a lower number: "))
upper = int(input("Enter an upper number: "))
for i in range(lower,upper+1):
    square = i*i
    print("The square of ",i," is ", square,".",sep="")
************************
