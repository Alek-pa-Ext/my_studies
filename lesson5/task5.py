from functools import reduce
from random import randint
numbers = [randint(-10, 10) for _ in range(5)]
result = reduce(lambda a, b: a * b, numbers)

print(numbers, result, sep='\n')