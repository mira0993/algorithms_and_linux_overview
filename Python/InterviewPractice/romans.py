'''
Write a program to convert a decimal number to roman numerals. (Convert an integer number to its equivalent roman numeral.)
I
II
III
IV
VI
VII
VIII
IX
X

MAX 5000
'''

#457
static_roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def get_partial_number(index, result):
    if result <= 3:
        return static_roman[index]*result
    if result == 4:
        return static_roman[index]+static_roman[index+1]
    if result == 5:
        return static_roman[index+1]
    if result <= 8:
        return static_roman[index+1]+(static_roman[index]*(result-5))
    if result == 9:
        return static_roman[index] + static_roman[index+2]

def int_to_roman(number):
    if number >= 4000:
        return 'int_to_roman supports from 1 to 3999 only'
    original = number
    roman = []
    div = 1000
    index = 6
    while number > 0:
        result = number // div
        if result > 0:
            roman.append(get_partial_number(index, result))
        number%=div
        div//=10
        index-=2
    print('{0} == {1}'.format(original, ''.join(roman)))

for i in range(1, 4000):
    int_to_roman(i)
