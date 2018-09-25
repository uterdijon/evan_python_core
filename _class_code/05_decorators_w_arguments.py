# DECORATORS WITH INPUT
# the important thing to remember is that the initial function gets
# *replaced* with the wrapper function - that's what the *function call*
# to decorator_func() returns.
# Therefore you need to pass the *same arguments* to the wrapper function
# that you want to pass to your initial function.


def decorator_func(initial_func):

    def wrapper_func(arg):
        output = f"feeder gave you some | {initial_func(arg)} | to eat."
        return output

    return wrapper_func


# @decorator_func
def feeder(food):
    return food


feeder = decorator_func(feeder)  # remember that this is the same as @...

me = feeder("apples")
print(me)
print()



# DECORATORS WITH **KWARGS

def decorator_func(initial_func):

    def wrapper_func(**kwargs):
        output = f"eat {initial_func(**kwargs)} and {initial_func(**kwargs)}."
        return output

    return wrapper_func


# @decorator_func
def feeder(**kwargs):
    healthy = kwargs["healthy"]
    unhealthy = kwargs["unhealthy"]
    return healthy + unhealthy


feeder = decorator_func(feeder)  # remember that this is the same as @...

me = feeder(healthy="apple", unhealthy="cake")
print(me)
print()



# DECORATORS WITH *ARGS

def decorator_func(initial_func):

    def wrapper_func(*args):
        output = "SHOPPING LIST:\n"
        for line in initial_func(*args).split("\n"):
            line = f"* {line}\n"
            output += line
        return output

    return wrapper_func


# @decorator_func
def feeder(*args):
    output = ""
    for item in args:
        output += f"{item}\n"
    return output


print(feeder("apple", "cake"))  # before decoration

feeder = decorator_func(feeder)  # doing @ explicitly

print(feeder("apple", "cake"))  # with decoration
