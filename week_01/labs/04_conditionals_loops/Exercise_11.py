'''
Apply a Cesar cipher of 7 to the 'secret' variable.

p.s.: http://www.montypython.net/scripts/dentist.php

'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

**************************
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
message = ""
for i in secret:
    num = ord(i)
    other_num = num + cipher
    other_letter = chr(other_num)
    message = message + other_letter
print(message)
*************************
