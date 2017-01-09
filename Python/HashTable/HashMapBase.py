from MapBase import MapBase
from UnsortedTableMap import UnsortedTableMap
from random import randrange

class HashMapBase(MapBase):
    '''
    Abstract base class for using hash-table with MAD method

    Multiple-Add-and-Divide (MAD)
    [(ai + b) mod p] mod N

    N = size of the bucket array
    p = prime number larger than N
    a,b = integers  in range [0, p-1], where a > 0
    i = hash(key)
    '''

    def __init__(self, cap=5, p=109345121):
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):
        pass

    def _bucket_delitem(self, j, k):
        pass

    def __len__(self):
        return self._n

    def _hash_function(self, k):
        return ((hash(k)*self._scale + self._shift) % self._prime) % len(self._table)

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table)//2:
            self._resize(2*len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, size):
        old = list(self.items())
        self._table = [None] * size
        self._n = 0
        for (k,v) in old:
            self[k] = v
