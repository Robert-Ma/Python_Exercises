"""
Exercise 21: Write a python program to push an item on the heap, then pop and return the smallest item from the heap.
"""

import heapq

heap = [1,2,4,3]
heapq.heapify(heap)
print(heap)
x = heapq.heappushpop(heap, 5)
print(heap)
print(x)
