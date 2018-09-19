'''
try
except
multiple except
else
finally
assert
raise
throwing exceptions
custom exceptions
'''


'''
try:
  x = 3
except ZeroDivisionError as zde:
    print("There was an error: ", zde)
except Exception as ex:
    print("there was an error: ", exc)
else:
    # Will execute if no error
    print("There were no errors.")
finally:
    # Will execute no matter what


try:
    assert

try:
    if (10 > 0):
        raise Exception("we are raising this exception.")
        '''

def divide(arg1, arg2):
    #try:
        #ßreturn_value = arg1/arg2
    #except Zero DivisionError as exc:
        #raise exc
    #else:
        #return return_value
    if (arg2 == 0):
        raise ZeroDivisionError("You cannot divide by zero.")
    else:
        return arg1/arg2

try:
    print(divide(10,0))
except ZeroDivisionError as zde:
    print(zde)

print(divide(10, 0))
