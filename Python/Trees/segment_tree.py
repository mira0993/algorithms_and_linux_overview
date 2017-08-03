'''
Let us consider the following problem to understand Segment Trees.

We have an array arr[0 . . . n-1]. We should be able to
1 Find the sum of elements from index l to r where 0 <= l <= r <= n-1
2 Change value of a specified element of the array to a new value x.
  We need to do arr[i] = x where 0 <= i <= n-1.

Representation of Segment trees
--------------------------------
1. Leaf Nodes are the elements of the input array.
2. Each internal node represents some merging of the leaf nodes.
   The merging may be different for different problems.
   For this problem, merging is sum of leaves under a node.
'''

class SegmentNode(object):

    def __init__(self, start_range, end_range, value=0):
        self.start = start_range
        self.end = end_range
        self.total = value

        self.l_child = None
        self.r_child = None


    def set_left_child(self, node):
        self.l_child = node
        self.recalculate()

    def set_right_child(self, node):
        self.r_child = node
        self.recalculate()

    def recalculate(self):
        self.total = 0
        if self.l_child:
            self.total += self.l_child.total
        if self.r_child:
            self.total += self.r_child.total

    def __str__(self):
        return '[{0}:{1}]={2} => is_leaf={3}'.format(
            self.start,
            self.end,
            self.total,
            (self.l_child is None and self.r_child is None)
        )

class SegmentTree(object):

    def __init__(self, array):
        self.count = len(array)
        self.root = None
        self.build(array)

    def build(self, array):
        def _build(array, start, end):

            if end < start:
                return None

            if end == start:
                return SegmentNode(start, end, array[start])

            half = start + ((end - start) // 2)
            left = _build(array, start, half)
            right = _build(array, half+1, end)

            node = SegmentNode(start, end, left.total+right.total)
            node.set_left_child(left)
            node.set_right_child(right)

            return node

        self.root = _build(array, 0, len(array)-1)

    def query_sum_range(self, start, end):
        '''
        Pseudo-code:

        int getSum(node, l, r)
        {
           if range of node is within l and r
                return value in node
           else if range of node is completely outside l and r
                return 0
           else
            return getSum(node's left child, l, r) +
                   getSum(node's right child, l, r)
        }
        '''

        def get_sum(node, left, right):

            if not node or left > node.end or right < node.start:
                return 0

            if node.start >= left and node.end <= right:
                return node.total

            return get_sum(node.l_child, left, right) + get_sum(node.r_child, left, right)

        return get_sum(self.root, start, end)

    def update_value(self, index, new_value):
        if index >= self.count:
            raise IndexError

        def _update(node, index, new_value):
            if node.start == node.end == index:
                node.total = new_value

            else:
                half = node.start + ((node.end - node.start) // 2)
                if index <= half:
                    _update(node.l_child, index, new_value)
                else:
                    _update(node.r_child, index, new_value)

                node.recalculate()

        _update(self.root, index, new_value)

    def __str__(self):
        if not self.root:
            return 'Empty Tree'

        tree = '---- Segment Tree ----\n'
        queue = [self.root]

        while queue:
            new_queue = []
            for node in queue:
                if node:
                    tree += str(node) + '\n'
                    if node:
                        new_queue.append(node.l_child)
                        new_queue.append(node.r_child)
            queue = new_queue
        return tree

array = [1,3,5,7,9,11]
tree = SegmentTree(array)
print(tree)
print('----- Queries -----')
print(tree.query_sum_range(2,4))
print(tree.query_sum_range(0,4))
print(tree.query_sum_range(3,5))

tree.update_value(2,12)
print(tree)
