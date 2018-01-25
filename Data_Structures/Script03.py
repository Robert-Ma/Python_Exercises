#!/usr/bin/env python3
"""
Exercise 5: Write a Python program to count the most common words in a dictionary.
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
"""

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

    return sortedItems[:top]



if __name__ == '__main__':
    print(list(count_words(words,5)))
