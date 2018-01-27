"""
Exercise 20: Write a Python program to push three items inot a heap and return
the smallest item from the heap. Also Pop return the smallest item form the heap.
"""

import heapq

heap = []
heapq.heappush(heap, 11)
heapq.heappush(heap, 10)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 3)

print('the smallest item:', heap[0])
print('Pop the smallest item', heapq.heappop(heap))
