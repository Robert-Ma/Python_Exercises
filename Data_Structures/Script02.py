#!/usr/bin/env python3

"""
Write a Python program to iterate over an enum class and display individual member and their value;
Write a Python program to display all the member name of an enum class ordered by their values.
Write a Python program to get all values from an enum class.
"""

from enum import Enum

class Country(Enum):
    Afghaistan = 93
    Albania    = 355
    Algeria    = 213
    Andorra    = 376
    Angola     = 244
    Antarctica = 672

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        else:
            return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        else:
            return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        else:
            return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            return NotImplemented

    def __repr__(self):
        return '(%s, %d)' % (self.name, self.value)

if __name__ == '__main__':
    for x in list(sorted(Country)):
        print(x.name, ':', x.value)

    # To get all values
    y = [item.value for item in Country]
    print(y)

