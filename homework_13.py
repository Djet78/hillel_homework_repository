# ---------------------- homework_13 ------------------------

import math


def cone_square_and_volume(radius, height):
    cone_volume = 1/3 * math.pi * radius**2 * height
    generatrix = math.sqrt(radius**2 + height**2)  # Образующая
    cone_square = math.pi * radius * (generatrix + radius)
    return cone_square, cone_volume


print("Input radius below:")
radius_input = int(input())
print("Input height below:")
height_input = int(input())

cone_squa, cone_vol = cone_square_and_volume(radius_input, height_input)
print("With a radius equal to " + str(radius_input) + " and height equal to " + str(height_input) +
      " cone volume equals " + str(round(cone_vol, 2)) + " and cone square equals " + str(round(cone_squa, 2)))
