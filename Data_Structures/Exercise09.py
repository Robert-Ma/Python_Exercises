"""
Exercise 9: Write a Python program to create an instance of an collections.OrderedDict using a given dictionary. Sort the dictionary
during the creation and print members of the dictionary in reverse order.
"""

from collections import OrderedDict

data = {'Afghanistan' : 93,
        'Albania'     : 355,
        'Algeria'     : 213,
        'Andorra'     : 376,
        'Angola'      : 244}

# sorted by names
orderedData = OrderedDict(sorted(data.items(), key = lambda x: x[0]))
print(orderedData)

# sorted by values in  revers order
orderedData2 = OrderedDict(sorted(data.items(), key = lambda x: x[1], reverse = True))
print(orderedData2)
