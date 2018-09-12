'''
Print out every prime number between 1 and 100.
'''

##############
def is_prime(number):
    prime = False
    for i in range(2,number):
        if number % i == 0:
            print(number,"is a not a prime number.")
            prime = False
            break
        else:
            prime = True

    if prime == True:
        print(number,"is a prime number.")

def list_primes(upper):
    for number in range(2,upper):
        is_prime(number)

list_primes(100)
##############
