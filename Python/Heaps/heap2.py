#!/usr/bin/python
'''
HEAP

This may work as MIN or MAX heap.

left-index   = (2 * n) + 1
right-index  = (2 * n) + 2
parent-index = (child_index - 1) // 2

Although the heap is a binary tree, we work with it inside of an array.
We use the forumlas above to calculate the index of the child and parent for
a specific node.

Improvement to use a Heapify() function to recover the heap property. It will
push up or push down a node
'''

class Heap_2():

    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap
        self.next = 0

    def left(self, index):
        '''
        Get left child index
        '''
        return (index * 2) + 1

    def right(self, index):
        '''
        Get right child index
        '''
        return (index * 2) + 2

    def parent(self, index):
        '''
        Get parent index
        '''
        return (index -1) // 2

    def _swap(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]


    def _push_up(self, index):
        '''
        Allows to keep the heap property in the data structure. It swaps
        nodes from index to root until the heap property is recovered.
        (Mostly used in inserts)
        '''

        parent = self.parent(index)

        while parent >= 0:
            if self.is_min_heap:
                if self.heap[parent] > self.heap[index]:
                    self._swap(parent, index)
                else:
                    break
            else:
                if self.heap[parent] < self.heap[index]:
                    self._swap(parent, index)
                else:
                    break

            index = parent
            parent = self.parent(index)

    def _push_down(self, index, last_index):
        '''
        It swaps nodes from index to last_index element  or until the heap property is
        recovered (Mostly used in deletes and heap sort)
        '''

        while True:
            left_i = self.left(index)
            right_i = self.right(index)

            if left_i > last_index:
                break

            if self.is_min_heap:
                if right_i > last_index or self.heap[left_i] < self.heap[right_i]:
                    smaller = left_i
                else:
                    smaller = right_i

                if self.heap[index] > self.heap[smaller]:
                    self._swap(index, smaller)
                else:
                    break

                index = smaller

            else:
                if right_i > last_index or self.heap[left_i] > self.heap[right_i]:
                    greater = left_i
                else:
                    greater = right_i

                if self.heap[index] < self.heap[greater]:
                    self._swap(index, greater)
                else:
                    break

                index = greater

    def heapify(self, index, last=None):
        parent = self.parent(index)
        if last is None:
            last = len(self.heap) - 1

        if self.is_min_heap:
            if parent >= 0 and self.heap[index] < self.heap[parent]:
                # Push up
                self._push_up(index)
            else:
                # Push down
                self._push_down(index, last)
        else:
            if parent >= 0 and self.heap[index] > self.heap[parent]:
                # Push up
                self._push_up(index)
            else:
                self._push_down(index, last)

    def insert(self, value):
        self.heap.append(value)
        last = len(self.heap) - 1
        self.heapify(last, last)

    def delete(self, index):
        len_heap = len(self.heap)

        if len_heap <= 0:
            return

        if len_heap == 1:
            self.heap = []
        else:
            self._swap(index, len_heap-1)
            self.heap.pop()
            self.heapify(index, len_heap-2)

    def convert_array(self, array):
        for element in array:
            self.insert(element)

    def size(self):
        return len(self.heap)

    def __str__(self):
        if self.is_min_heap:
            title = '*** Min Heap ***'
        else:
            title = '*** Max Heap ***'
        return title + '\n' +str(self.heap)


def heap_sort(arr):
    max_heap = Heap_2(is_min_heap=False)
    max_heap.convert_array(arr)
    last = max_heap.size() - 1
    print(max_heap)
    while last > 0:
        max_heap.heap[0], max_heap.heap[last] = max_heap.heap[last], max_heap.heap[0]
        last -= 1
        max_heap.heapify(0, last)
    return max_heap.heap

arr = [17,9,5,1,21,11,6,8,15]
h = Heap_2()
h.heap = arr
for i in range(len(arr)):
    h._push_up(i)
print(h)
