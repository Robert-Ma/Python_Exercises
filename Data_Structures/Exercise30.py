"""
Exercise 30: Write a Python program to create a LIFO queue.
"""

import queue

q = queue.LifoQueue()
[q.put(i) for i in range(5)]

while not q.empty():
    print(q.get())
