#!/usr/bin/env python3

"""
Write a Python program to find the class wise roll number from a tuple-of-tuples.
Using the python standard library: collections:
    1) namedtuple(): factory function for creating tuple subclasses with named fields
    2) deque: list-like container with fast appends and pops on either end
    3) Counter: dict subclass for counting hashable objects
    4) OrderedDict: dict subclass that remembers the order entrier were added
    5) defaultdict: dict subclass that calls a factory function to supply missing values
"""

from collections import defaultdict

classes = (('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1))
d = defaultdict(list)
for k, v in classes:
    d[k].append(v)

print(d.items())
