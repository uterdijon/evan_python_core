class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '%,%' % (self.x, self.y)
