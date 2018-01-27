"""
Exercise 29: Write a Python program to create a FIFO queue.
"""

import queue

q = queue.Queue()
[q.put(i) for i in range(5)]

while not q.empty():
    print(q.get())
