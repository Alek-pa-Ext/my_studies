from random import randint

numbers = [randint(-100, 100) for _ in range(50)]

neg_num = list(filter(lambda x: x < 0, numbers))

print(numbers, neg_num, sep='\n')