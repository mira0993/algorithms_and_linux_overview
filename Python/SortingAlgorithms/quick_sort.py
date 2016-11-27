#!/usr/bin/python
'''
QUICK SORT

1.  Choose an element as pivot.
2.  Determine the definitive position of the pivot.
3.  Place the elements that are less than the pivot, into its left.
4.  Place the elements that are great than the pivot, into its right.
5.  Repeat the steps above with the sub-array from the left and the sub-array
    from the right until the size of the array allows to sorty it manually.

How to do the partition?

1.  Choose the last element as pivot.
2.  Determine the position p1, of the first element that is not less than
    the pivot (from left to right).
3.  Determine the position p2, of the first element that is not greater than
    the pivot (from right to left).
4.  Did p2 & p1 crossed each other?
        - Swap the elements in p1 and pivot.
        - The position of the partition is p1
5.  If p2 & p1 didn't crossed each other:
        - Swap the elements in p1 and p2.
        - Go back to step 2 with the next p1 and p2.
'''

from array_generator import create_random_array, swap, show


def partition(array, left, right):
    pivot = array[right]
    p1 = left
    p2 = right - 1
    while True:

        while p1 < right:
            if array[p1] > pivot:
                break
            p1 += 1

        while p2 >= 0:
            if array[p2] < pivot:
                break
            p2 -= 1

        if p2 < p1:
            swap(array, p1, right)
            break

        swap(array, p1, p2)
        p1 += 1
        p2 -= 1

    return p1


def quick_sort(array, left_index, right_index):

    if right_index - left_index < 1:
        return

    if right_index - left_index == 1:
        if array[right_index] < array[left_index]:
            swap(array, right_index, left_index)
        #print(array[left_index:right_index+1])
        return

    p = partition(array, left_index, right_index)
    #print('pivot=%d %s' % (p, str(array[left_index:right_index+1])))

    quick_sort(array, left_index, p-1)
    quick_sort(array, p+1, right_index)



ARRAY_SIZE = 2000
START = -1000
END = 20000

array_before = create_random_array(ARRAY_SIZE, START, END)
array_after = array_before[:]
quick_sort(array_after, 0, ARRAY_SIZE - 1)
show(array_before, array_after, 'Quick Sort')
