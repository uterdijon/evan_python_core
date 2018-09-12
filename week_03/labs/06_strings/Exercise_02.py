'''
Complete Exercise 8.3 (p.95) from the textbook.

'''
def is_palindrome(_string):
    return _string == _string[::-1]

print(is_palindrome("hih"))
