def get_next_multiple(num):
    i = 1
    while True:
        yield num*i
        i += 1

if __name__ == "__main__":
    gen_multiple_of_two = get_next_multiple(2)
    for _ in range(10):
        print(next(gen_multiple_of_two))

    gen_multiple_of_thirteen = get_next_multiple(13)
    for _ in range(5):
        print(next(gen_multiple_of_thirteen))