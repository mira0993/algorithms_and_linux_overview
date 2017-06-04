

# Return the smallest k element in array

import heapq

def smallest(arr, k):
    # Convert array into min_heap
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(k)]

def smallest_manual(arr, k):
    max_heap = []
    len_h = 0

    def insert(heap, elem):
        heap.append(elem)
        index = len(heap) - 1
        parent = (index - 1) // 2

        while parent >= 0:
            if heap[index] > heap[parent]:
                heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
            parent = (index - 1) // 2

    def delete_root(heap):
        last = len(heap) - 1
        heap[0], heap[last] = heap[last], heap[0]
        heap.pop()
        index = 0
        while True:
            l = (index * 2) + 1
            r = (index * 2) + 2

            if l > last-1:
                break

            if r > last-1 or heap[l] > heap[r]:
                chosen = l
            else:
                chosen = r

            if heap[index] < heap[chosen]:
                heap[index], heap[chosen] = heap[chosen], heap[index]
            else:
                break
            index = chosen

    for elem in arr:
        if len_h < k:
            insert(max_heap, elem)
            len_h += 1
            print(max_heap)
        else:
            if max_heap[0] > elem:
                print('---', max_heap[0], elem)
                delete_root(max_heap)
                insert(max_heap, elem)

    print(max_heap)



arr = [17,9,5,1,21,11,6,8,15,12,4,46]
print(sorted(arr))
print(arr)
#print(smallest(arr, 5))
smallest_manual(arr, 5)
