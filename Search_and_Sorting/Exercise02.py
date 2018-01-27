"""
Exercise 02: Write a Python program for sequential search.
"""

def Sequential_Search(L, x):
    """
    Sequential Search. L must be a list.
    """

    if isinstance(L, list):
        pos = 0
        while pos < len(L):
            if L[pos] == x:
                return True
            else:
                pos += 1
        return False
    else:
        return "First prameter must be a list."

if __name__ == '__main__':
    L = [1,4,2,5,89,23,12]
    print(Sequential_Search(L, 4))
    print(Sequential_Search(L, 100))
    print(Sequential_Search((1,2,5,3), 2))

