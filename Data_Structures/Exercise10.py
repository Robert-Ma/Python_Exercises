"""
Exercise 10: Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
Just like Exercise 6 (Scirpt06.py) using collections.defaultdict.
"""

from collections import defaultdict

data = [('V', 1), ('VI', 2), ('V', 3), ('VI', 4), ('VII', 1)]
d = defaultdict(list)
for k, v in data:
    d[k].append(v)

print(d.items())
