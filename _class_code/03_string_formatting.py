# --------------------------------------------------------
# --------------- PYTHON STRING FORMATTING ---------------
# --------------------------------------------------------
import random

greeting = "hello"
name = ["laura", "tony"]

# --------------------------- F-STRINGS -----------------------------
# python f-strings allow us to enter variables and expressions,
# including function calls etc., and evaluate them inside of the string:
msg1 = f"{greeting}, {random.choice(name)}! hope you're well. see you {1 + 1}morrow"
print(msg1)

# -------------------------- STR.FORMAT() ----------------------------
# if you are working with versions of python that are older than 3.6
# then use str.format() instead:
msg2 = "{}, {}! hope you're well. see you {}morrow".format(greeting, random.choice(name), 1 + 1)
print(msg2)
# you can also pass an index to the {} in str.format()
print("{0} is different than {1} but the same as {0}".format("BASIL", 42))
# the advantage of f-strings over str.format() is that it is much better
# readable, especially with longer strings with many variables


# ------------------ STRING FORMATTING MINI-LANGUAGE ------------------
# inside of the curly braces {} you can use a mini-language to format
# the pieces of string that are injected, e.g.:
mini = f"{greeting:>20s}"
print(mini)
# this works both for f-strings and .format(). Read more on it here:
# https://docs.python.org/3/library/string.html#format-specification-mini-language


# ---------------------- HANDLING LONG STRINGS ------------------------
# two ways of breaking up strings into multiple lines:

# 1) escaping the newline character:
long_str1 = "check out this very long string that is full of wisdom \
so you should definitely keep reading all the way to the end!"
# to *escape* a character that has meaning in python, you use the
# backslash \ character before the character. here the character we are
# escaping is the "newline" (linebreak), so we don't really see it.
print(long_str1)

# 2) using multiple strings inside of parentheses:
long_str2 = ("hei there "
            "how are you?"
            " remember that this string is actually not so long!")
print(long_str2)
# the advantage of the parentheses version is that it allows us to
# indent the code. python essentially concatenates the different pieces
# to create one string, while above it simply continues the string.
# therefore it will have surprising consequences if you indent the str:

long_str3 = "check out this very long string that is full of wisdom \
            so you should definitely keep reading all the way to the end!"
print(long_str3)
