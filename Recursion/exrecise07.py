"""
exercise 07: Write a Python program to calculate the harmonic sum of n - 1.
"""

def harmonicSum(n):
    if n <= 0 or not isinstance(n, int):
        raise TypeError('Prameter must be a positive integer.')

    if n == 1:
        return 1.
    else:
        return 1 / float(n) + harmonicSum(n - 1)


if __name__ == '__main__':
    print(harmonicSum(7))
    print(harmonicSum(4))
    print(harmonicSum(1))
