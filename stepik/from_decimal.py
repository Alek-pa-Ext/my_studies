offset = ord('A') - 10

num_system = input('What number system do you want to convert to?\n')
while not num_system.isdigit():
    num_system = input('Please, write a base of number system - integer number\n')
base = int(num_system)
number = input('Enter the number to be converted\n')
while not num_system.isdigit():
    num_system = input('Please, write a base of number system - integer number\n')
rem = int(number)
digits = []
while rem >= base:
    digits.append(rem % base if (rem % base) < 10 else chr(rem % base + offset))
    rem = rem // base
digits.append(rem)
digits.reverse()
print(*digits, sep='')