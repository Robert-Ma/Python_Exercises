"""
Exreicise 8: Write a Python program to get the unique enumeration values.
enum:
    An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration,
    the members can be compared by identity, and the enumeration itself can be iterated over.
"""

from enum import Enum

class Countries(Enum):
    Afghanistan = 93
    Albania     = 355
    Algeria     = 213
    Andorra     = 376
    Angola      = 244
    India       = 355
    USA         = 213

for item in Countries:
    print(item.name,'\t', item.value)
