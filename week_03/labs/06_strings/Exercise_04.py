'''
Write a script that finds the first vowel in a a user inputted string.

'''
vowels = "aeiou"
your_word = str(input("Enter a word: "))
for c in your_word:
    if c in vowels:
        print("The first vowel in ",your_word," is ",c,".")
        break
