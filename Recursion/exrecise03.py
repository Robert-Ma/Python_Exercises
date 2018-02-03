"""
exercise 03: Write a Python program to get the factorial of a non-negative integer.
"""

def factorial(n):
    if n >= 0 and isinstance(n, int):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        raise TypeError('Prameter must be a non-negative integer.')


if __name__ == '__main__':
    print(factorial(5))
    print(factorial(0))
    print(factorial(1))
