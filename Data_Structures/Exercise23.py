"""
Exercise 23: Write a Python program to get the two largest and three smallest items form a dataset.
heapq.nlargest(n, iterable[, key])
    Return a list with the n largest elements from the dataset defined by iterable. key, if provided,
    specifies a function of one argument that is used to extract a comparison key from each eleememt
    in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
heapq.nsmallest(n, iterable[, key])
    Return a list the n smallest elements from the dataset defined by iterable. key, if provided,
    specifies a function of one argument that is used to extract a comparison key from each eleememt
    in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key)[:n]
"""

import heapq
data = [1,3,2,4,12,543,65,23,90]
print(heapq.nlargest(2, data))
print(heapq.nsmallest(3, data))
