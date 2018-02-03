"""
exercise 09: Write a Python program to calculate the value of
'a' to the power 'b'. Both 'a' and 'b' are non-negative integers.
"""

def power(a, b):
    if a < 0 or b < 0 or not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Prameters must be a non-negative integer.')

    if a == 0:
        return 0

    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

if __name__ == '__main__':
    print(power(3, 4))
    print(power(0, 2))
    print(power(0, 0))
    print(power(0, 1))
    print(power(1, 0))
