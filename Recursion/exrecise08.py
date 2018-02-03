"""
exercise 08: Write a Python program to calculate the geometric sum.
"""

def geometricSum(n):
    if n < 0 or not isinstance(n, int):
        raise TypeError('Prameter must be a non-negative integer.')
    if n == 0:
        return 1.
    else:
        return float(1.) / pow(2, n) + geometricSum(n - 1)

if __name__ == '__main__':
    print(geometricSum(7))
    print(geometricSum(4))
    print(geometricSum(1))
    print(geometricSum(0))
