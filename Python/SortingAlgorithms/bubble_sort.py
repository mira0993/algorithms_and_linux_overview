#!/usr/bin/python
'''
BUBBLE SORT

1.  Iterate from left to right, swapping adyacent elements if necessary. At the
    end, the greatest element is at the final position of the array.
2.  We repeat the step 1 withour comparing the last element from  the last i
    teration.
*   If in one iteration we don't swap any element, it means that the list
    already ordered.
'''

from array_generator import create_random_array, swap, show


def bubble_sort(array):

    array_size = len(array)

    for i in range(array_size):
        moved = False
        for j in range(1, array_size - i):
            if array[j] < array[j-1]:
                swap(array, j-1, j)
                moved = True
        if not moved:
            break

ARRAY_SIZE = 1000
START = -100
END = 20000

array_before = create_random_array(ARRAY_SIZE, START, END)
array_after = array_before[:]
bubble_sort(array_after)
show(array_before, array_after, 'Bubble Sort')
