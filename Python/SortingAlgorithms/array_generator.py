#!/usr/bin/python
from random import randint

def create_random_array(length, min_val, max_val, ordered=False):
    if ordered:
        return sorted([randint(min_val, max_val) for i in range(length)])
    return [randint(min_val, max_val) for i in range(length)]

def swap(array, index_a, index_b):
    array[index_a], array[index_b] = array[index_b], array[index_a]

def is_sorted(array):
    for index in range(1, len(array)):
        if array[index] < array[index-1]:
            return False
    return True

def show(original_array, sorted_array, title):
    print('---------- '+title.upper()+' ----------')
    print('*** Original Array ***')
    print(original_array)
    print('*** Sorted Array ***')
    print(sorted_array)
    print('---------------------------------------')
    print('is_sorted = '+str(is_sorted(sorted_array)))
    print('---------------------------------------')
