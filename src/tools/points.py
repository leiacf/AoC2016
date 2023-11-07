def calculate_manhattan(p, q):
    """ Calculating and returning the manhattan distance between two points, p and q. The function expects two points in 2D space, as lists"""

    return ( abs(p[0]-q[0]) + abs(p[1]-q[1]) )