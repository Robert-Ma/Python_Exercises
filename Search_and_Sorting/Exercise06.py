"""
Exercise06.py: Write a Python program to sort a list of elements
using shell sort algorithm.
In this script, using concrete gaps: [N/2], [N/4], [N/8], ..., 1.
The worst case time complexity is O(N^2).
"""


def shellSort(alist):
    if not isinstance(alist, list):
        raise TypeError('Prameter must a list.')
    N = len(alist)
    gap = int(N / 2)

    while gap > 0:
        for i in range(gap, N):
            temp = alist[i]
            j = i

            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        gap = int(gap / 2)
    return alist


if __name__ == '__main__':
    alist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    print(shellSort(alist))
    print(shellSort(()))
