import logging
from random import randrange

LOG_LEVEL = logging.INFO
logging.getLogger().setLevel(LOG_LEVEL)


class SkipList():
    '''
    See skipList sample here: http://www.geeksforgeeks.org/skip-list/
    '''

    class _skipItem:

        def __init__(self, k=None, v=None, start_sentinel=False, end_sentinel=False):
            self._key = k
            self._value = v
            self._above = None
            self._bellow = None
            self._prev = None
            self._next = None
            self._start_sentinel = start_sentinel
            self._end_sentinel = end_sentinel

        def __eq__(self, item):
            return self._key == item._key

        def __ne__(self, item):
            return not self._key == item._key

        def __lt__(self, item):
            return self._key < item._key

        def is_sentinel(self):
            return self._start_sentinel or self._end_sentinel

        def next(self):
            '''
            Return the position following p on the same level
            '''
            return self._next

        def prev(self):
            '''
            Return the position preceding p on the same level
            '''
            return self._prev

        def bellow(self):
            '''
            Return the position bellow p in the same tower
            '''
            return self._bellow

        def above(self):
            '''
            Return the position above p in the same tower
            '''
            return self._above

        def __str__(self):
            return '[%s]=%s prev:%s next:%s above:%s bellow:%s' % (
                    str(self._key),
                    str(self._value),
                    str(self._prev._key if self._prev else '-'),
                    str(self._next._key if self._next else '-'),
                    str(self._above._key if self._above else '-'),
                    str(self._bellow._key if self._bellow else '-'))


    def __init__(self):
        self.root = self.create_new_level()
        self.height = 0

    def should_insert_above(self):
        return randrange(1000000) % 2 == 0

    def create_new_level(self):
        start = self._skipItem(start_sentinel=True)
        end = self._skipItem(end_sentinel=True)
        start._next = end
        end._prev = start
        return start

    def add_level(self):
        new_level = self.create_new_level()
        self.root._above = new_level
        new_level._bellow = self.root
        self.root = new_level
        self.height += 1
        logging.debug('Added new level - h=%d' % self.height)

    def skip_search(self, k):
        node = self.root
        level = self.height

        while node:
            logging.debug('[Level[%s] - Key[%s]]' % (str(level), str(node._key)))
            if not node.is_sentinel() and node._key == k:
                return node
            next_node = node.next()
            if next_node:
                if not next_node.is_sentinel() and next_node._key <= k:
                    node = next_node
                else:
                    if node.bellow():
                        node = node.bellow()
                        level -= 1
                    else:
                        break
            else:
                if node.bellow():
                    node = node.bellow()
                    level -= 1
                else:
                    break
        return node

    def insert_after_prev(self, prev_node, k, v):
        new_node = self._skipItem(k, v)
        new_node._next = prev_node._next
        new_node._prev = prev_node
        new_node._next._prev = new_node
        prev_node._next = new_node
        return new_node

    def insert_item(self, k, v):
        closest_node = self.skip_search(k)
        if closest_node._key == k:
            closest_node._value = v
        else:
            pos = self.insert_after_prev(closest_node, k, v)
            tower_bellow = pos
            i = 0
            add_new_level = False
            while not add_new_level and self.should_insert_above():

                if i >= self.height:
                    self.add_level()
                    add_new_level = True

                while pos.above() is None:
                    pos = pos.prev()

                pos = self.insert_after_prev(pos.above(), k, v)
                pos._bellow = tower_bellow
                tower_bellow._above = pos
                tower_bellow = pos
                i += 1

    def delete_item(self, k):
        node = self.skip_search(k)
        if node and node._key == k:
            while node:
                prev_node = node.prev()
                next_node = node.next()
                prev_node._next = next_node
                next_node._prev = prev_node
                node = node.bellow()
        else:
            raise KeyError('Key Error: ' + repr(k))



    def printall(self):
        node = self.root
        logging.info('------------ SKIP LIST -----------------')
        while node:
            level_node = node
            level = []
            while level_node:
                level.append('[%s]=%s' % (level_node._key, level_node._value))
                level_node = level_node.next()
            node = node.bellow()
            logging.info(' '.join(level))
        logging.info('---------------------------------------')

    def __setitem__(self, k, v):
        self.insert_item(k, v)

    def __getitem__(self, k):
        node = self.skip_search(k)
        if node and node._key == k:
            return node._value
        raise KeyError('Key Error: ' + repr(k))

    def __delitem__(self, k):
        self.delete_item(k)

######### TESTS ##############
# skip = SkipList()
# skip.insert_item(35,35)
# skip.insert_item(40,40)
# skip.insert_item(52,52)
# skip.insert_item(2,2)
# skip.insert_item(15,15)
# skip.insert_item(12,12)
# skip.printall()
# skip.delete_item(15)
# skip.printall()
# ----------------------------
# skip = SkipList()
# skip[123] = 'how are you?'
# skip[34] = 34
# skip[2] = 'stuff'
# skip[0] = 'a lot of stuff'
# skip[234] = 234
# skip.printall()
# skip[2] = skip[2].upper()
# skip.printall()
# del skip[34]
# skip.printall()
##############################
