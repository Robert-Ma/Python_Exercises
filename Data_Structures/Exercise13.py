"""
Exercise 13: Write a Python program to get the array size of types unsigned integer and float.
The array library defined following codes:
    +-----------+--------------------+-------------------+-----------------------+
    | Type code | C Type             | Python Type       | Minimum size in bytes |
    +-----------+--------------------+-------------------+-----------------------+
    | 'b'       | signed char        | int               | 1                     |
    | 'B'       | unsigned char      | int               | 1                     |
    | 'u'       | Py_UNICODE         | Unicode character | 2                     |
    | 'h'       | signed short       | int               | 2                     |
    | 'H'       | unsigned short     | int               | 2                     |
    | 'i'       | signed int         | int               | 2                     |
    | 'I'       | unsigned int       | int               | 2                     |
    | 'l'       | signed long        | int               | 4                     |
    | 'L'       | unsigned long      | int               | 4                     |
    | 'q'       | signed long long   | int               | 8                     |
    | 'Q'       | unsigned long long | int               | 8                     |
    | 'f'       | float              | float             | 4                     |
    | 'd'       | double             | float             | 8                     |
    +-----------+--------------------+-------------------+-----------------------+
"""

from array import array

unsInt = array('I', [1,2,3,4,5])
print('unsigned integer array length: %d' % len(unsInt))
print('unsigned integer array size: %d' % unsInt.itemsize)

f = array('f', [1., 2., 3., 4., 5.])
print('float array length: %d' % len(f))
print('float array size: %d' % f.itemsize)
