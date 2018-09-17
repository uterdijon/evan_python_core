'''Write a definition for a class named Circle with attributes center and radius,
 where center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at (150, 100)
 and radius 75. Write a function named point_in_circle that takes a Circle and a
  Point and returns True if the
Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and
 returns True if the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle and
 returns True if any of the corners of the Rectangle fall inside the circle.
 Or as a more challenging version, return True if any part of the Rectangle falls
  inside the circle.
Solution: http: // thinkpython2. com/ code/ Circle. py'''

class Circle:
  pass

class Point:
    pass

my_circle = Circle()

my_circle.center = Point()

my_circle.center.x = 150
my_circle.center.y = 100
my_circle.radius = 75

blank = Point()
blank.x = 3.0
blank.y = 4.0

def distance_between_points(p1, p2):
    import math
    diff_x = p2.x - p1.x
    diff_y = p2.y - p1.y
    next_step = (diff_x ** 2) + (diff_y ** 2)
    d = math.sqrt(next_step)
    return d

def point_in_circle(circle, point):
    """
    Determines whether a given point is within a given circle.
    """
    d = distance_between_points(circle.center, point)
    if d <= circle.radius:
        return True
    else:
        return False

print(point_in_circle(my_circle, blank))

class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def rect_in_circle(circle, rectangle):
    rectangle.corner2 = Point()
    rectangle.corner2.x = rectangle.corner.x + rectangle.width
    rectangle.corner2.y = rectangle.corner.y + rectangle.height
    is_corner1_in_circ = point_in_circle(circle, rectangle.corner)
    is_corner2_in_circ = point_in_circle(circle, rectangle.corner2)
    if is_corner1_in_circ == True and is_corner2_in_circ == True:
        return True
    else:
        return False

print(rect_in_circle(my_circle, box))

def rect_circle_overlap(circle, rectangle):
    rectangle.corner2 = Point()
    rectangle.corner2.x = rectangle.corner.x
    rectangle.corner2.y = rectangle.corner.y + rectangle.height
    rectangle.corner3 = Point()
    rectangle.corner3.x = rectangle.corner.x + rectangle.width
    rectangle.corner3.y = rectangle.corner.y + rectangle.height
    rectangle.corner4 = Point()
    rectangle.corner4.x = rectangle.corner.x + rectangle.width
    rectangle.corner4.y = rectangle.corner.y
    is_corner1_in_circ = point_in_circle(circle, rectangle.corner)
    is_corner2_in_circ = point_in_circle(circle, rectangle.corner2)
    is_corner3_in_circ = point_in_circle(circle, rectangle.corner3)
    is_corner4_in_circ = point_in_circle(circle, rectangle.corner4)
    if (is_corner1_in_circ == True or is_corner2_in_circ == True or
        is_corner3_in_circ == True or is_corner4_in_circ == True):
        return True
    else:
        return False

print(rect_circle_overlap(my_circle, box))
