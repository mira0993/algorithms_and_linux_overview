from BNode import BNode
from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    '''
    AVL tree is a self-balancing Binary Search Tree (BST)
    where the difference between heights of left and right
    subtrees cannot be more than one for all nodes.
    '''

    def AVL_insert(self, parent, node, value):
        '''
        INSERT IN AVL TREE:

        1) Perform standard BST insert for w.
        2) Starting from w, travel up and find the first unbalanced node.
        Let z be the first unbalanced node, y be the child of z that comes on the path
        from w to z and x be the grandchild of z that comes on the path from w to z.
        3) Re-balance the tree by performing appropriate rotations on the subtree rooted with z.
        There can be 4 possible cases that needs to be handled as x, y and z can be arranged in 4 ways.
        Following are the possible 4 arrangements:
        a) y is left child of z and x is left child of y (Left Left Case)
        b) y is left child of z and x is right child of y (Left Right Case)
        c) y is right child of z and x is right child of y (Right Right Case)
        d) y is right child of z and x is left child of y (Right Left Case)

        ...
        1) Perform the normal BST insertion.
        2) The current node must be one of the ancestors of the newly inserted
        node. Update the height of the current node.
        3) Get the balance factor (left subtree height - right subtree height) of the current node.
        4) If balance factor is greater than 1, then the current node is
        unbalanced and we are either in Left Left case or left Right case.
        To check whether it is left left case or not, compare the newly
        inserted key with the key in left subtree root.
        5) If balance factor is less than -1, then the current node is unbalanced
        and we are either in Right Right case or Right Left case. To check
        whether it is Right Right case or not, compare the newly inserted
        key with the key in right subtree root.
        '''

        if node is None:
            self.root = BNode(value)
            return

        if value <= node.value:
            if node.left:
                self.AVL_insert(node, node.left, value)
            else:
                new_node = BNode(value, node)
                node.left = new_node
                
        else:
            if node.right:
                self.AVL_insert(node, node.right, value)
            else:
                new_node = BNode(value, node)
                node.right = new_node

        self.rebalance_tree(parent, node, value)

    def is_tree_balanced(self):
        if self.root:
            if abs(self.balance_factor(self.root)) > 1:
                return false
        return True

    def node_height(self, node):
        if not node:
            return 0
        return max(self.node_height(node.left), self.node_height(node.right)) + 1

    def balance_factor(self, node):
        '''
        The difference between heights of left and right
        subtrees cannot be more than one for all nodes.
        '''
        return self.node_height(node.left) - self.node_height(node.right)

    def rebalance_tree(self, parent, node, inserted_value):
        bf = self.balance_factor(node)

        if bf > 1:  # we have left_left_case or left_right_case
            if inserted_value <= node.left.value:
                if not parent:
                    self.root = self._left_left_case(node)
                elif parent.left and parent.left.value == node.value:
                    parent.left = self._left_left_case(node)
                else:
                    parent.right = self._left_left_case(node)
            else:
                if not parent:
                    self.root = self._left_right_case(node)
                elif parent.left and parent.left.value == node.value:
                    parent.left = self._left_right_case(node)
                else:
                    parent.right = self._left_right_case(node)
        elif  bf < -1:
            if inserted_value <= node.right.value:
                if not parent:
                    self.root = self._right_left_case(node)
                elif parent.left and parent.left.value == node.value:
                    parent.left = self._right_left_case(node)
                else:
                    parent.right = self._right_left_case(node)
            else:
                if not parent:
                    self.root = self._right_right_case(node)
                elif parent.left and parent.left.value == node.value:
                    parent.left = self._right_right_case(node)
                else:
                    parent.right = self._right_right_case(node)

    def _left_left_case(self, node):
        '''
        T1, T2, T3 and T4 are subtrees.
         z                                      y
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2
        '''
        print('left-left-case: '+ str(node))
        new_orig = node.left
        node.left = node.left.right
        new_orig.right = node
        return new_orig

    def _right_right_case(self, node):
        '''
  z                                y
 /  \                            /   \
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4
        '''
        print('right-right-case: '+ str(node))
        new_orig = node.right
        node.right = node.right.left
        new_orig.left = node
        return new_orig

    def _left_right_case(self, node):
        '''
     z                               z                           x
    / \                            /   \                        /  \
   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
T1   x                          y    T3                    T1  T2 T3  T4
    / \                        / \
  T2   T3                    T1   T2
        '''
        print('left-right-case: '+ str(node))
        node.left = self._right_right_case(node.left)
        return self._left_left_case(node)

    def _right_left_case(self, node):
        '''
   z                            z                            x
  / \                          / \                          /  \
T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
   x   T4                      T2   y                  T1  T2  T3  T4
  / \                              /  \
T2   T3                           T3   T4

        '''
        print('right-left-case: '+ str(node))
        node.right = self._left_left_case(node.right)
        return self._right_right_case(node)



# arr = [13,10,15,5,11,16,4,6]
# tree = AVLTree()
# tree.insert_from_array(arr)
# tree.AVL_insert(None, tree.root, 3)
# BinarySearchTree.inorder(tree.root)

# arr = [30,5,35,32,40]
# tree = AVLTree()
# tree.insert_from_array(arr)
# tree.AVL_insert(None, tree.root, 45)
# BinarySearchTree.inorder(tree.root)

# arr = [13,10,15,5,11,16,4,6]
# tree = AVLTree()
# tree.insert_from_array(arr)
# tree.AVL_insert(None, tree.root, 7)
# BinarySearchTree.inorder(tree.root)

arr = [5,2,7,1,4,6,9,3,16]
tree = AVLTree()
tree.insert_from_array(arr)
tree.AVL_insert(None, tree.root, 15)
BinarySearchTree.inorder(tree.root)
