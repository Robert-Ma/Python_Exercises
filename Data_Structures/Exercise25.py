"""
Exercise 25: Write a Python program to locate the right insertion point for a
specified value in sorted order.
"""

import bisect

x = [1,2,3,4,5,6,7]
print(bisect.bisect_right(x, 3))
print(bisect.bisect_left(x, 3))
