


class LNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.last = None

    def is_tail(self, data):
        return not self.next

    def __str__(self):
        str_val = '['+str(self.data)+']--'
        if self.next is None:
            str_val += '|'
        else:
            str_val += '>'
        return str_val


class SimpleLinkedList(object):

    def __init__(self, node_class):
        self.clazz = node_class
        self.root = None

    def insert_node(self, value):

        if self.root is None:
            self.root = self.clazz(value)
        else:
            node = self.root

            while node.next is not None:
                node = node.next
            node.next = self.clazz(value)

    def delete_node(self, value):
        node = self.root
        last = None

        while node:
            if node.data == value:
                if last:
                    last.next = node.next
                else:
                    self.root = self.root.next
                return True
            last = node
            node = node.next
        return False

    def fill_with_array(self, array):
        for i in array:
            self.insert_node(i)

    def print_list(self):
        node = self.root
        all_list = []
        while node is not None:
            all_list.append(str(node))
            node = node.next
        print(''.join(all_list))

array = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
simpleList = SimpleLinkedList(LNode)
simpleList.fill_with_array(array)
simpleList.print_list()
simpleList.delete_node('M')
simpleList.print_list()
simpleList.delete_node('D')
simpleList.print_list()
simpleList.delete_node('H')
simpleList.print_list()
simpleList.delete_node('F')
simpleList.print_list()
