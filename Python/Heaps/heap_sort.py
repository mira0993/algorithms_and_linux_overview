#!/usr/bin/python
'''
HEAP SORT

1.  Determine the greatest element and swap with the one at the end of the heap.
2.  The greatest element is already at its final position. This position won't be
    visited again. The end of the heap is now last-1.
3.  Push down the root node until we recover the heap property (all the child
    nodes should be less than the current node).
'''
import sys
sys.path.append('../')
from SortingAlgorithms.array_generator import create_random_array
from heap import Heap


def heap_sort(array, reversed_sort):
    my_heap = Heap(is_min_heap=reversed_sort)
    my_heap.convert_array(array)

    print('*** Original heap ***')
    my_heap.print_heap()

    last_index = my_heap.len_of_heap() - 1
    while last_index > 0:
        # Swap greatest element with the last element
        my_heap.swap_element(0, last_index)
        # Push down root node to recover heap property
        my_heap.push_down_node(current_index=0, last_index=last_index)
        # Change the last_index to one less
        last_index-=1

    print('*** Sorted heap ***')
    my_heap.print_heap()



test_array = create_random_array(10, 1, 100)
heap_sort([5,8,7,9,1,3], reversed_sort=True)
