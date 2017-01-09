from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+ repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+ repr(k))
        del bucket[k]


    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


    def __str__(self):
        values = []
        for index,bucket in enumerate(self._table):
            values.append('***** Bucket[%d]:' % index)
            values.append(str(bucket))
        return "\n".join(values)

#########  TESTS #############
# chainmap = ChainHashMap()
# chainmap['ab'] = 123
# chainmap['bc'] = 7634
# chainmap['cd'] = 234
# chainmap['de'] = 3243
# chainmap['ef'] = 4562
# chainmap['fg'] = 5674
# chainmap['gh'] = 678
# print(chainmap)
