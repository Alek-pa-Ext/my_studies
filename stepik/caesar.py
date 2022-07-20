def input_with_variants(message, variants, error_message):
    parameter = input(message)
    while parameter not in variants:
        parameter = input(error_message)
    return parameter

def caesar_cipher(start_text, key, offset, rev, power):
    fin_text = ''
    for cr in start_text:
        if cr.isalpha():
            start_num = ord(cr.lower()) - offset
            if cr.islower():
                fin_text += chr((start_num + key * rev) % power + offset)
            else:
                fin_text += chr((start_num + key * rev) % power + offset).upper()
        else:
            fin_text += cr
    return fin_text

direction = input_with_variants('Please, chose direction: encrypt - 1, decipher - 2\n',
                                ['1', '2'], 'Please, write 1 or 2\n')
rev = 1 if direction == '1' else - 1

language = input_with_variants('Please, chose the language: ru or en\n',
                               ['ru', 'en'], 'Please, write ru or en\n')

start_text = input('Please, write your text\n')


if language == 'ru':
    offset = ord('а')
    power = 32
else:
    offset = ord('a')
    power = 26

known_key = input_with_variants('Do you know a key? Write yes or no\n',
                                ['yes', 'no'], 'Please, write yes or no\n')

if known_key == 'yes':
    key = input('Please, write a key\n')
    while not key.isdigit():
        key = input('Please, write integer number\n')
    key = int(key)
    print(caesar_cipher(start_text, key, offset, rev, power))
else:
    for key in range(power):
        print(key, caesar_cipher(start_text, key, offset, rev, power))
