#numbers = Total elements (10M)
#n = Maximum n elements(In our case 10)

#Import Heap module in Python
import heapq

def findMaxN(n, numbers):
    if n == 0: return []
    heap = numbers[:n]
    #Transform list x into a heap, in-place, in linear time.
    heapq.heapify(heap)
    for k in numbers[n:]:
        if heap[0] < k:
            #Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised
            heapq.heapreplace(heap, k)
    return heap
