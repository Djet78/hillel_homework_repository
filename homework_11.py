# ---------------------- homework_12 ------------------------
import math


def degrees2radians(degrees):
    radians = (degrees * math.pi) / 180
    return radians


def radians2degrees(radians):
    degrees = (radians * 180) / math.pi
    return degrees


print("\ncos ⦟60° =", round(math.cos(degrees2radians(60)), 2), "\ncos ⦟45° = ", round(math.cos(degrees2radians(45)), 2),
      "\ncos ⦟40° = ", round(math.cos(degrees2radians(40)), 2))
