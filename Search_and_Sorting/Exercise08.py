"""
Exercise 08: Write a Python program to sort a list of elements
using quick sort algorithm.
"""

def quickSort(alist):
    """
    Quick sort algrithm, In-place version.
    """

    def partition(alist, left, right):
        pivot = alist[right - 1]
        i = left - 1
        for j in range(left, right):
            if alist[j] < pivot:
                i += 1
                (alist[i], alist[j]) = (alist[j], alist[i])
        if alist[right - 1] < alist[i + 1]:
            (alist[i + 1], alist[right - 1]) = (alist[right - 1], alist[i + 1])
        return i + 1

    def sort(alist, left, right):
        if left < right:
            storeIndex = partition(alist, left, right)
            sort(alist, left, storeIndex)
            sort(alist, storeIndex + 1, right)
    sort(alist, 0, len(alist))
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quickSort(alist))
    print(alist)

