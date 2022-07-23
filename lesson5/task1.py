from math import fabs
scale = lambda a, b: fabs(a * b)

print(scale(int(input()), int(input())))