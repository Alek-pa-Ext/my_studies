def triple_result(func):

    def act(*args):
        result = func(*args)
        return result * 3
    return act

if __name__ == "__main__":
    @triple_result
    def add(a, b):
        return a + b

    print(add(5, 5))