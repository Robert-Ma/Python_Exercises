"""
Write a Python program of recursion list sum.
"""

import collections

def recursiveSum(alist):
    listSum = 0
    for value in alist:
        if isinstance(value, collections.Iterable):
            listSum += recursiveSum(value)
        else:
            listSum += value
    return listSum


if __name__ == '__main__':
    alist = [1, 2, [3, 4], [5, 6], (7, 8)]
    print(recursiveSum(alist))
