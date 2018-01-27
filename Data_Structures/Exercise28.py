"""
exercise 28: Write a Python program to find whether a queue is empty or not.
"""

import queue

x = queue.Queue()
y = queue.Queue()

[x.put(i) for i in range(5)]
print('x is empty or not:', x.empty())
print('y is empty or not:', y.empty())
