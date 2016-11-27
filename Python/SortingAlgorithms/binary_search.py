#!/usr/bin/python
'''
BINARY SEARCH

We assume that the array is already sorted.

1.  Search for the value in the middle point.
2.  If it not there, the value hould be:
    - in the left half (if the value we are looking for is less than
    the one at the middle).
    - in the right half (if the value we are looking for is greater than
    the one at the middle).
2.  Look for the value in the chosen half.
3.  Repeat until we find the value.

'''

from array_generator import create_random_array, swap, show


def binary_search_recursive(array, search_val, min_index, max_index):

    if min_index > max_index:
        return False

    half_index = min_index +((max_index - min_index)//2)

    if array[half_index] == search_val:
        return True
    elif search_val < array[half_index]:
        return binary_search_recursive(array, search_val, min_index, half_index-1)
    else:
        return binary_search_recursive(array, search_val, half_index+1, max_index)

ARRAY_SIZE = 1000
START = -100
END = 20000
VAL = 89

array = [x for x in range(1, ARRAY_SIZE+1)]
found = binary_search_recursive(array, VAL, 0, ARRAY_SIZE-1)
print('--------- BINARY SEARCH ----------')
print('*** range: 1-'+str(ARRAY_SIZE))
print('*** found [%d]: %s' % (VAL, str(found)))
print('----------------------------------')
