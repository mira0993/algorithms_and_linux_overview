from BNode import BNode

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def height(self):
        def calc_height(node):
            if not node:
                return 0
            return max(calc_height(node.left), calc_height(node.right)) + 1
        if self.root:
            return calc_height(self.root)
        return 0

    @staticmethod
    def preorder(node):
        if not node:
            return
        print(node)
        BinarySearchTree.preorder(node.left)
        BinarySearchTree.preorder(node.right)

    @staticmethod
    def inorder(node):
        if not node:
            return
        BinarySearchTree.inorder(node.left)
        print(node)
        BinarySearchTree.inorder(node.right)

    @staticmethod
    def postorder(node):
        if not node:
            return
        BinarySearchTree.postorder(node.left)
        BinarySearchTree.postorder(node.right)
        print(node)

    def insert(self, value):

        if not self.root:
            self.root = BNode(value)
        else:
            node = self.root

            while True:
                if value <= node.value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = BNode(value, node)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = BNode(value, node)
                        break

    def insert_from_array(self, array):
        for i in array:
            self.insert(i)

    def find(self, value):
        node = self.root
        while node:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def remove(self, value):
        node_to_remove = self.find(value)
        if not node_to_remove:
            return False

        parent_node = node_to_remove.parent

        # Case 1: Node to remove is a leaf
        if node_to_remove.is_leaf():
            if parent_node.left.value == value:
                parent_node.left = None
            else:
                parent_node.right = None

        # Case 2: Node has only one child
        elif (node_to_remove.left and not node_to_remove.right) or \
           (node_to_remove.right and not node_to_remove.left):

            if parent_node.left.value == value:
                parent_node.left = node_to_remove.left if node_to_remove.left else node_to_remove.right
            else:
                parent_node.right = node_to_remove.left if node_to_remove.left else node_to_remove.right

        # Case 3: Node has two children
        # - Find min value in the right subtree
        # - Replace value to be deleted with min
        # - Remove the min duplicate in the right subtree
        elif node_to_remove.left and node_to_remove.right:
            min_node = self.find_min(node_to_remove.right)
            node_to_remove.value = min_node.value
            if min_node.parent.left.value == min_node.value:
                min_node.parent.left = None
            else:
                min_node.parent.right = None
        else:
            pass

        return True
