"""
exercise 10: Write a Python program to find the greatest common divisor (gcd)
of two positive integers.
"""


def gcd2(a, b):
    """
    Calculate the greatest common divisor of a and b.
    """
    if a <= 0 or b <= 0 or not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Prameters must be positive integers.')

    while b:
        (a, b) = (b, a % b)
    return a

if __name__ == '__main__':
    print(gcd2(12, 14))
    print(gcd2(12, 36))
