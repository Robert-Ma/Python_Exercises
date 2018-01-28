"""
Exercise 05: Write a Python program to sort a list of elements using the
insertion sort algorithm
"""

import operator

def insertionSort(alist, reverse=False):
    op = operator.lt if reverse else operator.gt
    i = 1
    while i < len(alist):
        j = i
        while j > 0 and op(alist[j - 1], alist[j]):
            alist[j - 1], alist[j] = alist[j], alist[j - 1]
            j -= 1
        i += 1
    return alist


if __name__ == '__main__':
    L = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    print(insertionSort(L))
    print(insertionSort(L, reverse=True))
