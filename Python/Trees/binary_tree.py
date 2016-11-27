#!/usr/bin/python
'''
BINARY TREE

It is a tree that allows maximum
'''

from node import BNode

class  BinaryTree(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = BNode(value)

        if not self.root:
            self.root = new_node
        else:
            elem = self.root
            while True:
                if new_node.data <= elem.data:
                    if elem.left:
                        elem = elem.left
                    else:
                        elem.left = new_node
                        break
                else:
                    if elem.right:
                        elem = elem.right
                    else:
                        elem.right = new_node
                        break

    def convert_array(self, array):
        for i in array:
            self.insert(i)

    def print_tree(self):
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            print(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    @staticmethod
    def get_height(node):
        if node is None or node.is_leaf():
            return 0
        return max(BinaryTree.get_height(node.left), BinaryTree.get_height(node.right)) + 1



    def find(self, value):
        node = self.root

        while node:
            if node.data == value:
                break
            if node.data < value:
                node = node.right
            else:
                node = node.left
        return node

    @staticmethod
    def preorder(node):
        if not node:
            return
        print(node)
        BinaryTree.preorder(node.left)
        BinaryTree.preorder(node.right)

    @staticmethod
    def inorder(node):
        if not node:
            return
        BinaryTree.inorder(node.left)
        print(node)
        BinaryTree.inorder(node.right)

    @staticmethod
    def postorder(node):
        if not node:
            return
        BinaryTree.postorder(node.left)
        BinaryTree.postorder(node.right)
        print(node)

#array = [45,23,1,5,56,25,88,21,75,90,89,100,3]
array = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
tree = BinaryTree()
tree.convert_array(array)
tree.print_tree()
n = tree.find('B')
print(BinaryTree.get_height(n))
print('preorder:')
BinaryTree.preorder(tree.root)
print('inorder:')
BinaryTree.inorder(tree.root)
print('postorder:')
BinaryTree.postorder(tree.root)
