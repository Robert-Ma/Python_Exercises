"""
Exercise 18: Write a Python program to read a string and interpreting the string as an array of machine values.
array.frombytes(s)
    Appends items from the string, interpreting the string as an array of machine values (as if it had been
    read from a file using the fromfile() method).
array.fromfile(f, n)
    Read n items (as machine values) from the file object f and append them to the end of the array. If less
    than n items are avaliable, EOFError is raised, but the items that were avaliable are still inserted inito
    the array. f must be a real built-in file object; something else with a read() method won't do.
array.fromlist(list)
    Append items from the list. This is equivalent to for x in list: a.append(x) except that if there is a type
    error, the array is unchanged.
array.fromstring()
    Deprecated alias for frombytes().
array.fromunicode(s)
    Extends this array with data from the given unicode string. The array must be a type 'u' array; otherwise a
    ValueError is raised. Use array.frombytes(unicodestring.encode(enc)) to append Unicode data to an array of some
    other type.
"""

from array import array
import binascii

x = array('i', [1,2,3,4,5])
print('array:', x)
y = x.tobytes()
print('bytes:', y)
z = array('i')
z.frombytes(y)
print('z from bytes:',z)
