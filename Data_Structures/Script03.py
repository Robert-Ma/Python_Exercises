#!/usr/bin/env python3
"""
Exercise 5: Write a Python program to count the most common words in a dictionary.
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
"""

from collections import OrderedDict, Counter
from operator import itemgetter
from pandas import DataFrame, Series

words = ['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
         'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
         'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
         'white', 'orange', "orange", 'red']

# Method 1: define a function
def count_words(sequences, num):
    """
    To count the most common words of sequences.
    sequences: sequences need to be counted
    num: return top num words.
    """

    counts = {}

    # To count words
    for x in sequences:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    items = counts.items()    # To get all items with tuple
    sortedItems = tuple(sorted(items, key = lambda element: (element[1],element[0]),reverse = True))    # To sort tuple by values
    # or using this:
    # sortedItems = [(words, count) for words, count in counts.items()].sort(key = lambda x: x[1])

    return sortedItems[:num]

# Mehtod 2: Use OrderedDict
def count_words2(Seq, num):
    """
    To count the most commom words of Seq using OrderedDict.
    """

    counts = {}
    for x in Seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    orderdCounts = OrderedDict(sorted(counts.items(), key = itemgetter(1), reverse = True))
    items = orderdCounts.items()

    return list(items)[:num]


if __name__ == '__main__':
    print(list(count_words(words,5))) # Using method 1
    print(count_words2(words, 4))     # Using method 2

    # Method 3: collections.Counter
    counts = Counter(words)           # Using collections.Counter
    print(counts.most_common(4))

    # Method 4: pandas.Series
    ser = Series(words)
    words_counts = ser.value_counts()
    print(words_counts[:4])
