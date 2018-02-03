"""
Exercise 01: Write a Python program to calcualte the sum of a list of numbers.
"""

def sumList(alist):
    """
    To calcualte the sum of a list of numbers.
    """

    sum = 0
    for value in alist:
        sum += value

    return sum

if __name__ == '__main__':
    alist = [2, 4, 5, 6, 7]
    print(sumList(alist))
    print(sum(alist))
