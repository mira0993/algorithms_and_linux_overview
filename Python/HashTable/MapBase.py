from collections import MutableMapping

class MapBase(MutableMapping):

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, item):
            return self._key == item._key

        def __ne__(self, item):
            return not self._key == item._key

        def __lt__(self, item):
            return self._key < item._key
