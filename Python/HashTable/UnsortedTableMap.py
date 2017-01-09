from MapBase import MapBase

class UnsortedTableMap(MapBase):
    '''
    Map implementation using an unordered list
    '''

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for index,item in enumerate(self._table):
            if item._key == k:
                self._table.pop(index)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __str__(self):
        values = []
        for item in self._table:
            values.append('[%s] %s' % (item._key, item._value))
        return '\n'.join(values)
