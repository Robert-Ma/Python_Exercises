"""
Exercise 22: Write  a Python program to create a heapsort, pushing all values
onto a heap and then popping off the smallest vlaues one at a time.
In fact, bisect.bisect is the best choice.
"""
import heapq
import bisect

def heapsort(x):
    heap = []
    for value in x:
        heapq.heappush(heap, value)

    return [heapq.heappop(heap) for i in range(len(heap))]

print(heapsort([1,2,3,4,2,3]))

# using bisect.bisect
heap = []
for i in [1,2,3,3,2,3]:
    bisect.insort(heap, i)
    print(heap)
