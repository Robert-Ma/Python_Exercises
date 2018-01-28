"""
Exercise 03: Write a Python program to sort a list of elements using the bubble
sort algorithm.
"""

def bubbleSort(aList):
    flag = False
    while not flag:
        flag = True
        n = 0
        for i in range(len(aList) - 1 - n):
            if aList[i] > aList[i + 1]:
                # swap the two elements
                (aList[i], aList[i + 1]) = (aList[i + 1], aList[i])
                flag = False
        n += 1
    return aList


if __name__ =='__main__':
    L = [5, 1, 4, 2, 8]
    print(bubbleSort(L))

    L2 = [1, 2, 4, 5, 8]
    print(bubbleSort(L2 ))

    L3 = [5, 1, 4, 1, 2, 8, 5]
    print(bubbleSort(L3))
