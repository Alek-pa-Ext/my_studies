def only_odd_arguments(func):

    def check(*args):
        for item in args:
            if item % 2 == 0:
                return 'Please add odd numbers!'
        return func(*args)
    return check

if __name__ == "__main__":
    @only_odd_arguments
    def add(a, b):
        return a + b

    @only_odd_arguments
    def multiply(a, b, c, d, e):
        return a * b * c * d * e

    print(add(4, 4))
    print(add(4, 5))
    print(add(5, 5))
    print(multiply(1, 2, 3, 4, 5))
    print(multiply(1, 1, 3, 3, 5))

