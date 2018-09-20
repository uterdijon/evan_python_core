# STEP ZERO - FUNCTIONS ARE FIRST-CLASS OBJECTS

# first make one, the second just for the list
def say_hi():
    print("Hi.")

say_hi()

hi = say_hi
hi()

def say_moo():
    print("moooooooo!")

_list = [say_hi, say_moo]
print(_list[0])
print(_list[0]())
_list = [say_hi(), say_moo()]

# STEP ONE - SCOPES REVISIT
def outer_func():
    msg = "Weeeeeekend!"

    def inner_func():
        print(msg)

    return inner_func

say_wee = outer_func()
say_wee()

# STEP TWO - PASSING A VARIABLE

def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

say_wee = outer_func("weee")
say_wee()

# STEP THREE - AN EMPTY DECORATOR (PASSING A FUNCTION)

def decorator_func(initial_func):
    def wrapper_func():
        return initial_func()
    return wrapper_func  # returns the wrapper func ready to be executed

def prettify():
    print("flowers and stuff")

decorated_pretty = decorator_func(prettify)
decorated_pretty()  # executes wrapper function which executes prettify() func

# STEP FOUR - LET'S CHANGE SOMETHING

def decorator_func(initial_func):
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func

@decorator_func  # exactly the same as the commented-out code below
def prettify():
    print("flowers for you")

# decorated_pretty = decorator_func(prettify)
# decorated_pretty()
prettify()  # @ fixes it to the function at definition time, so always there



# STEP FIVE - USE IT FOR MANY THINGS

def decorator_func(initial_func):
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func

@decorator_func
def prettify():
    print("flowers for you")

@decorator_func
def feed():
    print("apples and potatoes")

prettify()
feed()


# OUTLOOK: DJANGO

'''
Django (and many other web frameworks, e.g. Flask) use decorators within
the main workflow of their code.
E.g.:
- @login_required
- @require_http_methods


Other use cases:
- @logging
'''
