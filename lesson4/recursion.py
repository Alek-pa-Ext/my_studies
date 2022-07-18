from random import *

def find_min_ten(l, i=0, min_s=0, min_i=0):
    if i == 0:
        min_s = sum(l[i:i + 10])
        min_i = i
    if sum(l[i:i + 10]) < min_s:
        min_s = sum(l[i:i + 10])
        min_i = i
    if i < 91:
        print(i, 'iteration', min_s, 'min_i =', min_i)
        find_min_ten(l, i+1, min_s, min_i)
    else:
        print('min_i =', min_i)
        return min_i

if __name__ == "__main__":
    list = [randint(-128, 127) for _ in range(100)]
    print(list)
    res = find_min_ten(list)
    print(res)
    print(list[res:res + 10])
