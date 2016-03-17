import math

class Point(object):
    """ Represent a point in 2D space. """

def distance_between_points(p1, p2):
    """ Calculate distance between two Points. """
    x = abs(p1.x - p2.x) 
    y = abs(p1.y - p2.y) 
    return math.sqrt(x**2 + y**2) 

if __name__ == '__main__':
    point1 = Point()
    point2 = Point()
    point1.x, point1.y = 10.0, 4.0
    point2.x, point2.y = 7.0, 8.0
    print(distance_between_points(point1, point2))

