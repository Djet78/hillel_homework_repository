# ---------------------- homework_15 ------------------------
import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    """
    Func. checks circles intersect
    :param x1: coordinate x of first circle
    :param y1: coordinate y of first circle
    :param r1: radius of first circle
    :param x2: coordinate x of second circle
    :param y2: coordinate y of second circle
    :param r2: radius of second circle
    :return: True if the circles intersect or False if not
    """
    distance_between_circle_centres = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    radius_sum = r1 + r2
    radius_diff = abs(r1 - r2)
    if radius_sum < distance_between_circle_centres:
        return False
    elif radius_sum == distance_between_circle_centres:
        return True
    elif radius_diff < distance_between_circle_centres < radius_sum:
        return True
    elif distance_between_circle_centres == radius_diff:
        return True
    elif distance_between_circle_centres < radius_diff:
        return False
