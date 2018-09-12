'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''
your_string = str(input("Enter a message: "))
upper_string = your_string.upper()
lower_string = your_string.lower()
new_list = []
vowels = "aeiou"
for c in your_string:
    if c in vowels:
        c = c.lower()
    else:
        c = c.upper()
    new_list.append(c)
mixed_string = ''.join(new_list)

print(upper_string)
print(lower_string)
print(mixed_string)
