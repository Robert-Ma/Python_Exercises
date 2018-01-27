"""
Exercise 12: Write a Python program to create an array contains six integers. Also print all the members of the array.
The Python standard library array:
    This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point
    numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained.
    The type is specified object creation time by using a `type code`, which is a single character. The following type codes are defined:
    +-----------+--------------------+-------------------+
    | Type code | C Type             | Python Type       |
    +-----------+--------------------+-------------------+
    | 'b'       | signed char        | int               |
    | 'B'       | unsigned char      | int               |
    | 'u'       | Py_UNICODE         | Unicode character |
    | 'h'       | signed short       | int               |
    | 'H'       | unsigned short     | int               |
    | 'i'       | signed int         | int               |
    | 'I'       | unsigned int       | int               |
    | 'l'       | signed long        | int               |
    | 'L'       | unsigned long      | int               |
    | 'q'       | signed long long   | int               |
    | 'Q'       | unsigned long long | int               |
    | 'f'       | float              | float             |
    | 'd'       | double             | float             |
    +-----------+--------------------+-------------------+
"""

from array import array

x = array('h', [10, 20, 30, 40, 50])
for i in x:
    print(i)
