'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random

def guess_the_number():
    guessed_correct = False
    random_number = random.randint(1, 100)
    while guessed_correct == False:
        guessed_number = int(input("I am thinking of a number between 1 and 100. Guess the number: "))
        if guessed_number == random_number:
            print("Congratulations! You have guessed the correct number!")
        else:
            print("Sorry, that isn't the correct number.")
            guessed_number = True

guess_the_number()
