#!/usr/bin/python
'''
INSERTION SORT

1.  Move an element E to the left until finding an smaller element K than E.
2.  We assume that the elements from  the left are already ordered.
'''

from array_generator import create_random_array, swap, show


def insertion_sort(array):

    array_size = len(array)

    for i in range(1, array_size):
        value_to_move = array[i]
        j = i
        while j > 0:
            if array[j-1] <= value_to_move:
                break
            array[j] = array[j-1]
            j-=1
        array[j] = value_to_move

ARRAY_SIZE = 1000
START = -100
END = 20000

array_before = create_random_array(ARRAY_SIZE, START, END)
array_after = array_before[:]
insertion_sort(array_after)
show(array_before, array_after, 'Insertion Sort')
