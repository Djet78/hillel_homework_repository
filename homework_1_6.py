import math

# ------------------------------------------------------------
#                             basic hw
# ------------------------------------------------------------

a = float(13.2)
b = float(7.0)
c = float(2.4)

# -------------------------- Task 1 ---------------------------

print("\n" + ("_-_-_-" * 10))
result = a + b * (c / 2)
print("\ntask №%d) variable a = %.2f, variable b = %.2f, variable c = %.2f\n expression = %s\n result = %.2f"
      % (1, a, b, c, "a + b * (c / 2)", result))
print("\n" + ("_-_-_-" * 10))

# -------------------------- Task 2 ---------------------------

print("\n" + ("_-_-_-" * 10))
result = (a**2 + b**2) % 2
print("\ntask №%d) variable a = %.2f, variable b = %.2f, variable c = %.2f\n expression = %s\n result = %.2f"
      % (2, a, b, c, "(a**2 + b**2) % 2", result))
print("\n" + ("_-_-_-" * 10))

# -------------------------- Task 3 ---------------------------

print("\n" + ("_-_-_-" * 10))
result = (a + b)/12 * c % 4 + b
print("\ntask №%d) variable a = %.2f, variable b = %.2f, variable c = %.2f\n expression = %s\n result = %.2f"
      % (3, a, b, c, "(a + b)/12 * c % 4 + b", result))
print("\n" + ("_-_-_-" * 10))

# -------------------------- Task 4 ---------------------------

a = float(4)
b = float(17.3)
c = float(3.4)

print("\n" + ("_-_-_-" * 10))
result = (a - b*c) / (a + b) % c
print("\ntask №%d) variable a = %.2f, variable b = %.2f, variable c = %.2f\n expression = %s\n result = %.2f"
      % (4, a, b, c, "(a - b*c) / (a + b) % c", result))
print("\n" + ("_-_-_-" * 10))

# -------------------------- Task 5 ---------------------------

print("\n" + ("_-_-_-" * 10))
result = abs(a - b) / (a + b)**3 - math.cos(c)
print("\ntask №%d) variable a = %.2f, variable b = %.2f, variable c = %.2f\n expression = %s\n result = %.2f"
      % (5, a, b, c, "| a - b | /( a + b)³ - cos( c )", result))
print("\n" + ("_-_-_-" * 10))

# -------------------------- Task 6 ---------------------------

print("\n" + ("_-_-_-" * 10))
result = (math.log(1 + c) / b)**4 + abs(a)
print("\ntask №%d) variable a = %.2f, variable b = %.2f, variable c = %.2f\n expression = %s\n result = %.2f"
      % (6, a, b, c, "( ln( 1 + c ) / -b )**4 + | a |", result))
print("\n" + ("_-_-_-" * 10))
