"""
exercise 06: Write a Python program to calculate the sum of the positive integers of
n + (n - 2) + (n - 4) + (n - 6) ... (until n - x <= 0).
"""

def seriesSum(n):
    if n < 0 or not isinstance(n, int):
        raise TypeError('Prameter must be a positive integer.')

    if n == 0:
        return 0
    else:
        return n + seriesSum(n - 2)

if __name__ == '__main__':
    print(seriesSum(6))
