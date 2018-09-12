'''
Complete Exercise 3.2 (p.27) from the textbook.

'''
*********************
def print_twice(bruce):
    print(bruce)
    print(bruce)
def do_twice(f,x):
    f(x)
    f(x)
def print_spam():
    print('spam')
def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)
do_four(print,'spam')
*********************
