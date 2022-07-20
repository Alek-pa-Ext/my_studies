from random import *

def find_min_ten(l, i=0, min_i=0):
    if i == len(l) - 9:
        return min_i
    else:
        if sum(l[i:i + 10]) < sum(l[min_i:min_i + 10]):
            min_i = i
        return find_min_ten(l, i+1, min_i)

if __name__ == "__main__":
    list = [randint(-128, 127) for _ in range(100)]
    print(list)
    print(find_min_ten(list))

