"""
Exercise 14: Write a Python program to get an array buffer information.
array.itemsize
    The length in bytes of noe array item in the internal representation.
array.buffer_info()
    Return a tuple (address, length) giving the current memory address and the length in element of
    the buffer used to hold array's contents. The size of the memory buffer in bytes can be computed
    as array.buffer_info()[1] * array.itemsize. This is occasionally useful when working with low-level
    (and inherently unsafe) I/O inferfaces that require memory address, such as certain ioctl() operations.
    The returned numbers are valid as long as the array exists and no length-changing operations are applied to it.

"""

from array import array

arr = array("d", [1,2,3,4])
print("The array memory address and the length:", arr.buffer_info())
print("The size of the memory buffer in bytes: ", arr.buffer_info()[1] * arr.itemsize)
