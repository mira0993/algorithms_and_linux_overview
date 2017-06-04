'''
Sort 100 million 10 bit integers.

10 bits = 0-1023 decimal
'''

import random

def sort(arr):
    repetitions = [0 for _ in range(1024)]

    for i in arr:
        repetitions[i] += 1
    index = 0
    for n in range(1024):
        for r in range(repetitions[n]):
            arr[index] = n
            index += 1

def is_sorted(arr):
    last = 0
    for i in range(len(arr)):
        if arr[i] < last:
            return False
        last = arr[i]
    return True
test = [random.randrange(0,1024) for _ in range (pow(10,7))]
sort(test)
print(is_sorted(test))
