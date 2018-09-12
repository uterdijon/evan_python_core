'''
Demonstrate the use of the "break" statement to exit a loop.

'''
***************************
#This program determines whether a given letter is in a given word.

letter = input("Enter a letter: ")
word = input("Enter a word: ")
inWord = False
for i in word:
    if i == letter:
        print("The letter ",letter," is in the word ",word,".",sep="")
        inWord = True
        break
if not inWord:
    print("The letter ",letter," is not in the word ",word,".",sep="")
***************************
