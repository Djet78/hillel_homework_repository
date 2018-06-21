# ------------------------ Task 35 -------------------------


class Circle:

    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def is_point_in_circle(self, point):
        return (point.x - self.x)**2 + (point.y - self.y)**2 <= self.rad**2


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


circle_1 = Circle(7, 14, 5)
point_1 = Point(7, 19)

print(circle_1.is_point_in_circle(point_1))
