"""
Exercise 09: Write a Python program for counting sort.
"""

def countingSort(alist):
    if not isinstance(alist, list):
        raise TypeError('Prameter must be a list.')

    count = [None] * len(alist)
    for i in range(len(alist)):
        p = 0
        q = 0
        for j in range(len(alist)):
            if alist[j] < alist[i]:
                p += 1
            elif alist[j] == alist[i]:
                q += 1
        for k in range(p, p + q):
            count[k] = alist[i]
    return count


if __name__ == '__main__':
    alist = [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1]
    print(countingSort(alist))
    print(countingSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
