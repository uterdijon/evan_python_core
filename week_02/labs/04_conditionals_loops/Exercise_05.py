'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''
******************************
lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))
sum = 0
tally = 0
for number in range(lower,upper+1):
    sum += number
    tally += 1
average = sum / tally
print("The sum of all the numbers between ",lower," and ",upper," is: ",sum,".",sep="")
print("The average of all the numbers between ",lower," and ",upper," is: ",average,".",sep="")       
******************************
