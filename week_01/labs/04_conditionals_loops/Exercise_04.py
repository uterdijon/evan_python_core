'''
Print out every prime number between 1 and 100.

'''
***************
for number in range(2,100):
    for i in range(2,number):
        if number % i == 0:
            print(number,"is not a prime number.")
            break
        else:
            print(number,"is a prime number.")
            break
***************
