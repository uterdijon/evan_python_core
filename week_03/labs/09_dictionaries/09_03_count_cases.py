'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1


'''

import string
text = input("Enter a sentence: ")
tally = {'upper': 0, 'lower': 0, 'punct': 0, 'total': 0}
for char in text:
    if char.isupper():
        tally['upper'] +=1
    elif char.islower():
        tally['lower'] += 1
    elif char in string.punctuation:
        tally['punct'] += 1
tally['total'] = tally['upper'] + tally['lower'] + tally['punct']
return

print(tally)
print(tally['upper'])
print(tally['lower'])
print(tally['punct'])
print(tally['total'])
    
        
