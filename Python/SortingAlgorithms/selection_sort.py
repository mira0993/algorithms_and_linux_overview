#!/usr/bin/python
'''
SELECTION SORT

1.  Find the smallest element in the array and then swap that element with the
    one in the first position.
2.  Find the second smallest element and swap it for the one in the second
    position.
3.  Repeat this for each element of the array.
'''

from array_generator import create_random_array, swap, show


def selection_sort(array):

    array_size = len(array)

    for i in range(array_size):
        min_index = i
        for j in range(i+1, array_size):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            swap(array, i, min_index)

ARRAY_SIZE = 100
START = -100
END = 20000

array_before = create_random_array(ARRAY_SIZE, START, END)
array_after = array_before[:]
selection_sort(array_after)
show(array_before, array_after, 'Selection Sort')
