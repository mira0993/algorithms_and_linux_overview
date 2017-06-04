'''
You are going to write a class. The class is passed an array that looks
like this: [3, 8, 1, 4, 0, 7, 2, 5] (0-based array).
Then even entries tell you how many times the
odd entries are to be repeated as you decode this array.
So e.g. in this case, the array inflates to "8,8,8,4,5,5".
Write your class to support an iterator,
so that each time it's called, it returns the next element in the sequence.
So for example, in this case, the first 3 times it's called it returns "8",
the 4th time it's called it returns "4", and so forth.
'''

def easy_approach(arr):
    for index in range(0,len(arr), 2):
        for _ in range(arr[index]):
            yield arr[index+1]


ITER_STATE = {'index': -2, 'count': 0}
def manual_approach(arr):
    while True:
        if ITER_STATE['index'] >= len(arr):
            raise StopIteration

        if ITER_STATE['count'] <= 0:
            ITER_STATE['index'] += 2
            if ITER_STATE['index'] < len(arr):
                ITER_STATE['count'] += arr[ITER_STATE['index']]

        if ITER_STATE['count'] > 0:
            ITER_STATE['count'] -= 1
            return arr[ITER_STATE['index']+1]



arr = [3, 8, 1, 4, 0, 7, 2, 5]
while True:
    print(manual_approach(arr))
