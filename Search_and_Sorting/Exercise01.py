"""
Exercise01: Write a Python program for binary search.
"""

def binary_search(itemList, item):
    """
    For binary search. If found the target value, return its position, or return False.
    """
    first = 0
    last = len(itemList) - 1

    while(first <= last):
        mid = (first + last) // 2
        if itemList[mid] == item:
            return mid
        else:
            if item < itemList[mid]:
                last = mid -1
            else:
                first = mid + 1
    return False


if __name__ == '__main__':
    print(binary_search([1,2,3,4,5], 6))
    print(binary_search([1,2,3,4,5], 5))
    print(binary_search([1,2,3,4,5,6], 3))
    print(binary_search([1,2,3,4,5], 1))
    print(binary_search([1,2,3,4], 0))
    print(binary_search((1,2,3,4), 6))
