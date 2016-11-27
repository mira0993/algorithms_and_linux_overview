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
'''

class Heap():

    def __init__(self, is_min_heap=True):
        self.heap = []
        self.min_heap = is_min_heap
        self.next = 0

    def convert_array(self, array):
        for i in array:
            self.insert_node(i)

    def insert_node(self, value):

        # Get index of value to be inserted
        current = self.next
        # Insert new value
        self.heap.append(value)
        # Match heap rules:
        self.push_up_nodes(current)
        self.next+=1

    def push_up_nodes(self, current_index):

        start_index = current_index
        parent_index = self.get_parent_index(start_index)

        while parent_index >= 0:
            #print('parent[%d]: %d - current[%d]: %d ' % (parent_index, self.heap[parent_index], start_index, self.heap[start_index]))
            if self.min_heap:
                if self.heap[parent_index] > self.heap[start_index]:
                    self.swap_element(parent_index, start_index)
                    #print('swapped: '+ str(self.heap))
                else:
                    break
            else:
                if self.heap[parent_index] < self.heap[start_index]:
                    self.swap_element(parent_index, start_index)
                    #print('swapped: '+ str(self.heap))
                else:
                    break

            start_index = parent_index
            parent_index = self.get_parent_index(start_index)

    def push_down_node(self, current_index, last_index):
        '''
        This method is used for the heap sort only
        '''

        start_index = current_index

        while True:
            left_index = self.get_left_child_index(start_index)
            right_index = self.get_right_child_index(start_index)

            if left_index == -1 or left_index >= last_index:
                break

            if self.min_heap:
                if right_index == -1 or right_index >= last_index or self.heap[left_index] < self.heap[right_index]:
                    smaller_index = left_index
                else:
                    smaller_index = right_index

                if self.heap[start_index] > self.heap[smaller_index]:
                    self.swap_element(start_index, smaller_index)
                else:
                    break

                start_index = smaller_index

            else:
                if right_index == -1 or right_index >= last_index or self.heap[left_index] > self.heap[right_index]:
                    greatest_index = left_index
                else:
                    greatest_index = right_index

                if self.heap[start_index] < self.heap[greatest_index]:
                    self.swap_element(start_index, greatest_index)
                else:
                    break

                start_index = greatest_index

    def get_left_child_index(self, current_index):
        index = (2 * current_index) + 1
        if index >= self.next:
            return -1
        return index

    def get_right_child_index(self, current_index):
        index = (2 * current_index) + 2
        if index >= self.next:
            return -1
        return index

    def get_parent_index(self, current_index):
        if current_index == 0:
            return -1
        return (current_index -1) // 2

    def len_of_heap(self):
        return len(self.heap)

    def swap_element(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

    def print_heap(self):
        print(self.heap)
