# https://www.reddit.com/r/learnpython/comments/3w3vkk/whats_the_difference_between_raising_an_exception/


def foo():
    raise Exception("challenge starts here!")


def bar():
    spam = foo()  # this assignment, and anything below, never executes
    return eggs(spam)  # would fail, bc it doesn't even exist


def baz():
    # -------- EXCEPTION HAPPENS (and bubbles up) --------
    # uncommenting the line below, instead of using the try-except block,
    # leads to our Exception being *raised* (= our script terminates
    # with showing our custom Exception message)
    # print(bar())  # <----- uncomment this!

    # -------- ERROR HANDLING --------
    # using the try-except construct as below (= catching the Exception)
    # allows us to *register* that an Exception occurred, e.g. we are
    # printing out the associated message we passed above,
    # yet *still continue with the execution of our script*!
    try:
        print(bar())
    except Exception as e:
        print(e)


baz()
# quote: "So then this exception gets passed up the stack until it
# reaches something to handle it and then execution continues from that
# elevated point?" - - - yep ;)
print("we here")  # only prints when the Exception is caught with except
