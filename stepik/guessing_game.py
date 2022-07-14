from random import randint
def get_value(key, dictionary):
    for value in dictionary:
        if key in dictionary[value]:
            return value

print("Let's play a game!")
print('Try to guess a number from 1 to 100!')

again = True

while again:
    rand_num = randint(1, 100)
    not_win = True
    how_close = {
        'Very very far!': [i for i in range(80, 100)],
        'Too far.': [i for i in range(60, 80)],
        'Not close.': [i for i in range(40, 60)],
        'Close.': [i for i in range(20, 40)],
        'Very close.': [i for i in range(5, 20)],
        'Almost hit!': [i for i in range(1, 5)]
    }

    while not_win:
        n = input('Write your number\n')
        while not n.isdigit() or int(n) not in range(1, 101):
            print('Your number is invalid')
            n = input('Please write integer number between 1 and 100\n')
        n = int(n)
        if n == rand_num:
            print('Congratulation! You win!')
            not_win = False
        if n > rand_num:
            print(get_value(n - rand_num, how_close), 'You need lower. Try again!')
        if n < rand_num:
            print(get_value(rand_num - n, how_close), 'You need higher. Try again!')

    again = False

    answer = input('Do you want to play again? Print "yes" or "no"\n')
    while answer not in ['yes', 'no']:
        answer = input("I don't understand, write again\n")
    if answer == 'yes':
        again = True