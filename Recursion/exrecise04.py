"""
exercise 04: Write a Python program to solve the Fibonacci sequence
using recursion.
"""

def fibonacci(n):
    if n > 0 and isinstance(n ,int):
        if n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        raise TypeError('Prameter must be a non-negative integer.')


if __name__ == '__main__':
    print(fibonacci(10))
