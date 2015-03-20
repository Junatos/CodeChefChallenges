__author__ = 'arjunkumar'

# solution to http://www.codechef.com/problems/INTEST/

# simple brute force
import sys

n, k = map(int, input().split())
c = 0

for line in sys.stdin:
    if int(line) % k == 0:
        c += 1

print(c)

'''
I could have used memoization to count number of occurrences of a number using a dictionary:
21333 -> 3
5453  -> 2
212   -> 1
..
.
Then checked the value only once instead of multiple times

count = 0
for key,value in dict:
    if key % k == 0:
        count += value
'''
