#!/usr/bin/python


class BNode():

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def is_leaf(self):
        if not self.left and not self.right:
            return True
        return False

    def __str__(self):
        l = r = 'none'
        if self.left:
            l = str(self.left.data)
        if self.right:
            r = str(self.right.data)
        return '* '+str(self.data)+'=> L:'+l+'  R:'+r
