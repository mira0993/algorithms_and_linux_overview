#!/usr/bin/python
'''
MERGE SORT

1.  If the array has a minimum size, then order it manually and return it.
2.  Create two-subarrays from the original one (helf left, helf right).
3.  Sort the sub-arrays calling the same method.
4.  Merge both arrays and return the result.
'''

from array_generator import create_random_array, swap, show


def merge(array_a, array_b):
    merged_array = []

    index_a = 0
    index_b = 0

    while index_a < len(array_a) and index_b < len(array_b):

        if array_a[index_a] < array_b[index_b]:
            merged_array.append(array_a[index_a])
            index_a += 1
        else:
            merged_array.append(array_b[index_b])
            index_b += 1

    for i in range(index_a, len(array_a)):
        merged_array.append(array_a[i])

    for i in range(index_b, len(array_b)):
        merged_array.append(array_b[i])

    return merged_array

def sort(array):

    if len(array) <= 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            swap(array, 0, 1)
        return array

    half = len(array) // 2

    array_a = sort(array[:half])
    array_b = sort(array[half:])
    return merge(array_a, array_b)



ARRAY_SIZE = 10000
START = -100
END = 20000

array_before = create_random_array(ARRAY_SIZE, START, END)
array_after = sort(array_before)
show(array_before, array_after, 'Merge Sort')
