"""
Exercise 26: Write a Python program to insert items into a list in sorted order.
"""

import bisect
import random

data = [random.randint(1,100) for i in range(15)]
print('data:', data)

sortedData = []
[bisect.insort(sortedData, i) for i in data]
print(sortedData)


