'''
Given an integer, write a function that turns it into an English string
(123,456 -> "one hundred twenty three thousand, four hundred fifty six")
'''

str_repr = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'thirteen',
    '15': 'thirteen',
    '16': 'thirteen',
    '17': 'thirteen',
    '18': 'thirteen',
    '19': 'thirteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninty',
}

def  get_english_str(number):
    arr = []
    count = 0
    current_str = ''

    if number == 0:
        return 'zero'

    while number > 0:
        arr.append(str(number%10))

        if len(arr) == 3:
            count += 1
            current_str = get_partial_str(arr, count) + current_str
            arr = []

        number//=10

    if arr:
        current_str = get_partial_str(arr, count+1) + current_str

    print(current_str)

def get_partial_str(arr, count):
    UNIT = 0
    TEN = 1
    HUNDRED = 2
    partial = ''
    for i in range(len(arr)):
        if arr[i] == '0':
            continue
        elif i == UNIT:
            partial = str_repr[arr[i]]
        elif i == TEN:
            num = arr[i]+arr[i-1]
            if num in str_repr:
                partial = str_repr[num]
            else:
                partial = str_repr[arr[i]+'0'] + ' ' + partial
        elif i == HUNDRED:
            partial = str_repr[arr[i]] + ' hundred ' + partial

    if count % 2 == 0:
        partial += ' thousand, '
    if count == 3:
        partial += ' million, '
    return partial

get_english_str(1000421711)
