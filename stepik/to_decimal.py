offset = ord('A') - 10

num_system = input('What number system do you want to convert from?\n')
while not num_system.isdigit():
    num_system = input('Please, write a base of number system - integer number\n')
base = int(num_system)
number = input('Enter the number to be converted\n')
digits = []
for c in number:
    if c.isdigit():
        digits.append(int(c))
    else:
        digits.append(ord(c) - offset)
digits.reverse()
result = 0
for i in range(len(digits)):
    result += digits[i] * base**i
print(result)