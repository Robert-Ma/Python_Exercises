"""
Exercise 11: Write a Python program to compare two unordered lists (not sets).
Compared by each value pairs, or compared by summary using collections.Counter.
"""

from collections import Counter

# Compared by each value pairs
def compare_lists_pairs(x, y):
    if isinstance(x, list) and isinstance(y, list):
        print('prameters must be list')
        return False

    if len(x) != len(y):
        return False
    else:
        # sort x and y
        sortedX = sorted(x, reverse = False)
        sortedY = sorted(y, reverse = False)

        for a,b  in zip(sortedX,sortedY):
            if a != b:
                return False
        return True

# Compared by collections.Counter
def compare_lists_counter(x, y):
    return Counter(x) == Counter(y)

if __name__ == '__main__':
    n1 = [20, 10, 30, 10, 20, 30]
    n2 = [30, 20, 10, 30, 20, 50]

    print(compare_lists_pairs(n1, n2))
    print(compare_lists_counter(n1, n2))
