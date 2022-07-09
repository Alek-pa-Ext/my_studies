n = input('Please write integer number between 1 and 100\n')
while not n.isdigit() or int(n) not in range(1, 101):
    print('Your number is invalid')
    n = input('Please write integer number between 1 and 100\n')
n = int(n)
fizz_mult = 3
buzz_mult = 5
if n % fizz_mult == 0:
    print('Fizz', end='')
if n % buzz_mult == 0:
    print('Buzz', end='')