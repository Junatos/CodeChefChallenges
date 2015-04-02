__author__ = 'Jun'

# solution to http://www.codechef.com/problems/TSORT

'''
Now I could have used the simple list.sort() function that python provides,
but I wanted to implement merge sort in python because I've done it for every
other language I've learned. Unfortunately merge sort takes too much time for such
a limited size input array. After some searching I decided to go for Counting Sort.
Remember our input size is limited at  [t <= 10^6].

SIGH looks like anything that doesn't use list.sort() which is implemented in C is
a no go for py 3.1.2. How boring.
'''

import sys

unsorted_list = map(int, sys.stdin.read().split()[1:])

print('\n'.join(map(str, sorted(unsorted_list))))