

class BNode():
    '''
    Basic node to use in a binary tree
    '''

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def is_leaf(self):
        if not self.left and not self.right:
            return True
        return False

    def __str__(self):
        left_repr = str(self.left.value if self.left else None)
        right_repr = str(self.right.value if self.right else None)
        return '[%s]<-[%s]->[%s]' % (left_repr, self.value, right_repr)
