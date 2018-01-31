"""
Exercise 8: Write a Python program to sort a list of elements using
the merge sort algorithm.
"""

import operator

def mergeSort(alist, reverse=False):
    if not isinstance(alist, list):
        raise TypeError('Prameter must be a list.')
    op = operator.gt if reverse else operator.lt
    if len(alist) > 1:
        mid = int(len(alist) / 2)
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf, reverse)
        mergeSort(rightHalf, reverse)

        i = j =k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if op(leftHalf[i], rightHalf[j]):
                alist[k] = leftHalf[i]
                i += 1
            else:
                alist[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j += 1
            k += 1
    return alist

if __name__ == '__main__':
    alist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    print(mergeSort(alist, reverse=True))
    print(mergeSort(alist))
