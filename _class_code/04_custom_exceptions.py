e = Exception()
print(vars(e)) # this is empty {}
print(dir(e)) # still contains all the dunders
print(e) # doesn't print anything, unless the __str__ is defined
print(repr(e))  # 'Exception()'
print(e.__str__) # '<method-wrapper '__str__' of Exception object at 0x103950f10>'
print("\n\n")


# ----------------------------------------------------------------------


class MyException(Exception):
    status_codes = {404: "not found", 500: "server error"}

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        self.status_message = MyException.status_codes[status_code]

    def __str__(self):
        return f"{self.status_code}: {self.message}"


x = 10
y = 0

try:
    if (y == 0):
        raise MyException(404, "this is wrong")
    print(x / y)
except MyException as e:
    print(f"error with status code: {e.status_code}")
    print(f"with message: {e.message}")
    print(e.status_message)
