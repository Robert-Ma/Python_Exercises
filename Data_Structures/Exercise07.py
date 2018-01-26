#! /usr/bin/env python3
"""
Write a Python program to count the number of students of individual class.
Now, it's time to use collections.Counter.
Counter objects support methods:
    1) elements()
       Return an itertor over elements repeating each as many times as its count. Elements are returnedin arbitrary order.
       If an element's count is less than one, elements() will ignore it.
    2) most_common([n])
       Return a list of the n most common elements and their counts from the most common to the least.
       If n is omitted or None, most_common() returns all elements in the counts. Elements with equal counts are ordered arbitrary.
    3) subtract([iterable-or-mapping])
       Elements are subtract from an iterable or from another mapping (or counter). Like dict.update() but subtract counts instead
       of replacing them. Both inputs and outputs may be zero or negative.
"""

from collections import Counter

classes = (('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1))
d = Counter([name for name, _ in classes])
print(d)

# elements()
print("list all elements:\n", list(d.elements()))
# most_common()
print("list most common:\n", d.most_common(2))
# subtract()
c = Counter({'V':2, 'VI':2, 'VII':3})
c.subtract(d)
print("subtract:\n", c)
