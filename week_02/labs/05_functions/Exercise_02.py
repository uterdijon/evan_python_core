'''
Complete Exercise 3.3 (p.27) from the textbook.

'''

*****************************
tel_pole = "+----+----+"

sticks = "||| ||| ||| |||"
    
def draw_tel_pole():
    print(tel_pole,end=" ")
    
def draw_sticks():
    print(sticks,end=" ")
    
def draw_pattern():
    print(tel_pole,end=" ")
    print(sticks,end=" ")
    
def do_twice(f):
    f()
    f()

def draw_grid():
    do_twice(draw_pattern)
    draw_tel_pole()
    
draw_grid()

*****************************

tel_pole = "+----+----+"

sticks = "||| ||| ||| |||"
    
def draw_tel_pole():
    print(tel_pole,end=" ")
    
def draw_sticks():
    print(sticks,end=" ")
    
def draw_pattern():
    print(tel_pole,end=" ")
    print(sticks,end=" ")
    
def do_twice(f):
    f()
    f()

def draw_grid():
    do_twice(draw_pattern)
    draw_tel_pole()
    print("")
    
def do_four(f):
    do_twice(f)
    do_twice(f)

def draw_big_grid():    
    do_four(draw_grid)

draw_big_grid()

*****************************
