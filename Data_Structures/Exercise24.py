"""
Exercise 24: Write a Python program to locate the left insertion point for a
specified value in sorted order.
The Python Standard Library: bisect -- Array bisection algorithm
This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion. For long lists of items with
expensive comparison operations, this can be an improvement over the more
commom approach. The module is called bisect because it uses a basic bisection
algorithm to do its work. The source code may be most useful as a working
example of the algorithm (the boundary conditions are already right!).
The following functions are provided:
bisect.bisect_left(a, x, lo=0, hi=len(a))
    Locate the insertion point for x in a to maintain sorted order. The
    parameters lo and hi may be used to specify a subset of the list which
    shoud be considered; by default the entire list is used. If x is already
    present in a, the insertion point will be before (to the left of) any
    exsting entires. The return value is suitable for use as the first
    parameter to list.inset() assuming that a is already sorted.
    The returned insertion point i partitions the array a into two helves so
    that all(val < x for val in a[lo:i]) for the left side and all(val >= x for
    val in a[i:hi]) for right side.
bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x, lo=0, hi=len(a))
    Similar to bisect_left(), but returns an insertion point which comes after
    (to the right of) any existing entires of x in a.
bisect.insort_left(a, x, lo=0, hi=len(a))
    Insert x in a in sorted order. This is equivalent to
    a.insert(bisect.bisect_left(a, x, lo, hi), x) assuming that a is already
    sorted. Keep in mind that the O(log n) search is dominated by the slow
    O(n) insertion step.
bisect.insort_right(a, x, lo=0, hi=len(a))
bisect.insort(a, x, lo=0, hi=len(a))
    Similar to insort_left(), but inserting a in a after any existing entires
    of x.
"""

import bisect

x = [1,2,3,4,5]
print(bisect.bisect_left(x, 4))  # output is 3
print(bisect.bisect_right(x, 4)) # output is 4
