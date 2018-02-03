"""
exercise 05: Write a Python program to get the sum of a non-negative integer.
"""

# using recursion
def sumInteger(n):
    if n < 0 or not isinstance(n, int):
        raise TypeError('Prameter must be a non-negative integer.')

    if n == 0:
        return 0
    else:
        return n % 10 + sumInteger(int(n / 10))

# using list
def sumIntegerList(n):
    if n < 0 or not isinstance(n, int):
        raise TypeError('Prameter must be a non-negative integer.')

    return sum([int(value) for value in list(str(n))])


if __name__ == '__main__':
    print(sumInteger(12345))
    print(sumIntegerList(12345))



