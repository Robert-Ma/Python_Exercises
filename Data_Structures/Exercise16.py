"""
Exercise 16: Write a Python program to convert an array to an ordinary list with the same items.
array.tolist()
   Convert the array to an ordinary list with the same items.
array.tostring()
   Deprecated alias for tobytes().
array.tobytes()
   Convert the array to an array of machine values and  return the bytes representation (the same
   sequence of bytes that would be written to file by the tofile() method.)
array.tofile()
   Write all items (as machine values) to  the file object f.
array.tounicode()
    Convert the array to a unicode string. The array must be a type 'u' array; otherwise a ValueError
    is raised. Use array.tobytes().decode(enc) to obtain a unicode string froma an array of some other type.
"""

from array import array

arr = array('i', [1,2,3,4,5,6])
print('Array:', arr)
print('List:', list(arr))
print('array.tolist():', arr.tolist())
