'''
Read the documentation of the string methods at:
http://docs.python.org/3/library/stdtypes.html#string-methods.
You might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

Demonstrate below:

- strip: Removes the characters in the argument from the string.
####################
new_string = 'My name is Evan.'
new_string = new_string.strip('M')
print(new_string)
>>> y name is Evan.
####################

- replace: Replaces first argument with second.
####################
my_string = "My name is Evan".replace('Evan','Peter')
print(my_string)
>>> My name is Peter.
####################

- find: returns index of first instance of string passed as argument.

####################
my_string = 'My name is Evan'.find('Evan')
print(my_string)
>>> 11
'''
Source: Exercise in chapter "Strings" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2009.html
####################
'''
