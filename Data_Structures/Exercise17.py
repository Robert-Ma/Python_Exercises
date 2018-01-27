"""
Exercise 17: Write a Python program to convert an array to an array of machine values and return the bytes representation.
array.tobytes()
    Convert the array to an array of machine values and return the bytes representation (the same sequence of bytes that
    would be written to a file by the tofile() method.)
"""

from array import array
import binascii

arr = array('i', [1,2,3,4,5,6])
print('array:', arr)
print('machine values:', arr.tobytes())
print('bytes:', binascii.hexlify(arr.tobytes()))
