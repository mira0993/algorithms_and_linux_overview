

class IntervalNode(object):

    def __init__(self, low_value, high_value):
        self.low = low_value
        self.high = high_value
        self.max = high_value

        self.left = None
        self.right = None

    def height(self):
        def _height(node):
            if not node:
                return 0
            return max(_height(node.left), _height(node.right)) + 1

        return _height(self)

    def left_height(self):
        if not self.left:
            return 0
        return self.left.height()

    def right_height(self):
        if not self.right:
            return 0
        return self.right.height()

    def balance_factor(self):
        return self.left_height() - self.right_height()

    def __str__(self):
        return '[{0},{1}] => {2}  is_leaf={3}'.format(
            self.low,
            self.high,
            self.max,
            (self.left is None and self.right is None)
        )

class IntervalTree(object):

    def __init__(self):
        self.root = None

    def right_rotate(self, node):
        tmp_node = node.left
        node.left = tmp_node.right
        tmp_node.right = node
        return tmp_node

    def left_rotate(self, node):
        tmp_node = node.right
        node.right = tmp_node.left
        tmp_node.left = node
        return tmp_node

    def left_rotate_right_rotate(self, node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_rotate_left_rotate(self, node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def rebalance_tree(self, parent, node, value):
        balance_factor = node.balance_factor()

        # left-left-case (right rotation)
        # left-right-case (left rotation, right rotation)
        if balance_factor > 1:
            if node.left and value <= node.left.low:
                if not parent:
                    self.root = self.right_rotate(node)
                elif parent.left and parent.left == node:
                    parent.left = self.right_rotate(node)
                else:
                    parent.right = self.right_rotate(node)
            else:
                if not parent:
                    self.root = self.left_rotate_right_rotate(node)
                elif parent.left and parent.left == node:
                    parent.left = self.left_rotate_right_rotate(node)
                else:
                    parent.right = self.left_rotate_right_rotate(node)
        # right-right-case (left rotation)
        # right-left-case (right rotation, left rotation)
        elif balance_factor < -1:
            if node.right and value > node.right.low:
                if not parent:
                    self.root = self.left_rotate(node)
                elif parent.left and parent.left.value == node:
                    parent.left = self.left_rotate(node)
                else:
                    parent.right = self.left_rotate(node)
            else:
                if not parent:
                    self.root = self.right_rotate_left_rotate(node)
                elif parent.left and parent.left.value == node:
                    parent.left = self.right_rotate_left_rotate(node)
                else:
                    parent.right = self.right_rotate_left_rotate(node)

    def insert(self, interval):

        def _insert(parent, node, low, high):
            if node is None:
                self.root = IntervalNode(low, high)
                return

            if low <= node.low:
                if node.left:
                    _insert(node, node.left, low, high)
                else:
                    node.left = IntervalNode(low, high)
            else:
                if node.right:
                    _insert(node, node.right, low, high)
                else:
                    node.right = IntervalNode(low, high)

            self.rebalance_tree(parent, node, low)
            if node.max < high:
                node.max = high

        _insert(None, self.root, interval[0], interval[1])

    def query_overlap_intervals(self, low, high):

        def _query(node, low, high, intervals):
            if not node:
                return

            if (low >= node.low and low <= node.high) or (high >= node.low and high <= node.high):
                intervals.append([node.low, node.high])

            if node.left and node.left.max > low:
                _query(node.left, low, high, intervals)

            if node.right and node.right.max > low:
                _query(node.right, low, high, intervals)

        intervals = []
        _query(self.root, low, high, intervals)
        return intervals

    def __str__(self):
        nodes = []
        queue = [self.root]

        while queue:
            new_queue = []
            for node in queue:
                if node:
                    nodes.append(str(node))
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            queue = new_queue

        return '---- Interval Tree ----\n' + '\n'.join(nodes)


intervals = [[15,20], [10,30], [17,24], [5,13], [12,15], [30, 40]]

interval_tree = IntervalTree()
for interval in intervals:
    interval_tree.insert(interval)

print(interval_tree)
print(21,33,interval_tree.query_overlap_intervals(21,33))
print(14,18,interval_tree.query_overlap_intervals(14,18))
