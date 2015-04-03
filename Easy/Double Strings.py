__author__ = 'arjunkumar'

# solution to http://www.codechef.com/problems/DOUBLE
import sys

n, *lengths = map(int, sys.stdin.buffer.read().split())

# let's add some memoization for fun woooo
lookup = {}

for i in range(n):
    if i not in lookup:
        if lengths[i] % 2 == 0:
            lookup[i] = lengths[i]
        else:
            lookup[i] = lengths[i] - 1
    print(lookup[i])