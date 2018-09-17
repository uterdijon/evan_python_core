'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''
import math
class Point:
    pass
""" Represents a point in 2-D space. """

blank = Point()
blank.x = 3.0
blank.y = 4.0

blink = Point()
blink.x = 8.0
blink.y = 2.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
    diff_x = p2.x - p1.x
    diff_y = p2.y - p1.y
    next_step = (diff_x ** 2) + (diff_y ** 2)
    d = math.sqrt(next_step)
    return d

print(distance_between_points(blink, blank))

print_point(blank)

class Rectangle:
    pass
''' Represents a rectangle.

attributes:
    attributes: width, height, corner. '''

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy



move_rectangle(box, 3, 4)
print(box.corner.x)

import copy
box2 = copy.copy(box)
print(box2.corner is box.corner)

def move_copy_rectangle(rect, dx, dy):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2

box2 = move_copy_rectangle(box, 2, 3)
print(box2.corner.x)
