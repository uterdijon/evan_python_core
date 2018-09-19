'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
try:
    with open('/Users/evan/CodingNomads/test/new_venv/python_core/week_04/labs/03_exception_handling/integers.txt', 'r') as f:
        number = f.readline()
        newval = number + 1
        #assert type(number) == int

except IOError as file_exc:
    print("File does not exist!")

except TypeError as typ_exc:
    print("You can only use integers for this!")

else:
    result = number * 4
    print(result)
