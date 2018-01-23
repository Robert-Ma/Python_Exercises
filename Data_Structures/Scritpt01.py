#!/usr/bin/env python3
"""
Write a Python program to create an Enum object and display a number name and value.
Pacakge enum:
    An enumeration is a set of symbolic names (members) bound to unique, constant values.
    Within an enumeration, the members can be compared by identity, and the enumeration
    itself can be iterated over. The enum members have names and values.
"""

from enum import Enum

class Country(Enum):
    Afhanistan = 93
    Albania    = 355
    Algeria    = 213
    Andorra    = 376
    Angola     = 244

if __name__ == "__main__":
    print("Member name: %s" % (Country.Afhanistan.name))
    print("Member value: %s" % (Country.Afhanistan.value))
    print(Country['Albania'])
    print(repr(Country['Albania']))
    print(list(Country))
    for item in Country:
        print(item.name,'\t', item.value)

