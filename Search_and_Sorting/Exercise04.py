"""
Exercise 04: Write a Python program to sort a list of elements using
the selection sort algorithm.
"""

import operator

def selectionSrot(alist, reverse = False):
    oper = operator.gt if reverse else operator.lt
    for i in range(len(alist)):
        flagIndex = 0
        for j in range(len(alist) - i):
            if oper(alist[flagIndex], alist[j]):
                flagIndex = j
        (alist[flagIndex], alist[len(alist) - 1 - i]) = (alist[len(alist) - 1 -i], alist[flagIndex])
    return alist



if __name__ == '__main__':
    L = [14, 46, 43, 27, 57, 41, 45, 21, 70, 43]
    print(selectionSrot(L))
    print(selectionSrot(L, reverse=True))


