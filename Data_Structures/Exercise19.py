"""
Exercise 19: Write a Python program to push three items inot the heap and print the items from the heap.
The Python Standared Library heapq:
    This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
    The following functions are provided:
    heapq.heappush(heap, item)
        Push the value item onto the heap, maintaining the heap invariant.
    heapq.heappop(head)
        Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised.
    heapq.heappushpop(heap, item)
        Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than
        heappush() followed by a seperate call to heappop().
    heapq.heapify(x)
        Transfrom list x into a heap, in-place, in linear time.
    heapq.heapreplace(heap, item)
        Pop and return the smallest item from the heap, and also push the new item. The heap size doesn't change. If the heap is emapty,
        IndexError is raised. This is more efficient than heappop() followed heappush(), and can be more appropriate when using a fixed-size
        heap. Note that the value returned may be larger than item!
"""

import heapq

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
print(heap)
while heap:
    print(heapq.heappop(heap))
    # In fact, heap is a list, but don't use it as list
