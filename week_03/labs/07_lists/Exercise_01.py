'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))
e = int(input("Enter another number: "))
f = int(input("Enter another number: "))
g = int(input("Enter another number: "))
h = int(input("Enter another number: "))
i = int(input("Enter another number: "))
j = int(input("Enter another number: "))

numbers = [a, b, c, d, e, f, g, h, i, j]

sum = 0
tally = 0

for num in numbers:
    sum += num
    tally += 1

avg = sum / tally

print("The sum is: ", sum)
print("The average is: ", avg)
