__author__ = 'arjunkumar'

# solution to http://www.codechef.com/problems/FCTRL

'''
Thinking:
10 = 2 * 5
10 = 10 * 1

2! = 2
5! = 5 * 2 * 4 * 3
6! = 5 * 2 * 6 * 4 * 3
10!= 10 * 5 * 2 * 9 * 8 * 7 * 6 * 4 * 3

So 0's can be added to the end using 2 * 5 pairs or 10s
More 0s can be added to the end using 20 * 50 pairs or 100s
More 0s can be added to the end using 200 * 500 pairs or 1000s and so on

So... find number of 10^n 10^n-1.... 10
Add n n-1 n-2 ... 0s to the end

Find how many 10s the number has i.e 20 has two 10s, 100 has ten 10s etc.
Add a 0 for each (this should take care of the 2*5 for each 10)

Test run: 20! = 2432902008176640000
Has two occurrences 10s in the form of 2*5s -> Add 2 0s
Has two occurrences of 10 ^ 1 in the form of 10,20 -> Add 2 0s
Worked this time
I can already see this breaking for 25!

Test run: 1024! = ...253 0s
Has one occurrence of 10 ^ 3 -> Add 3 0s
Has ten occurrences of 10 ^ 2 -> Add 10 0s
Has hundred + 2 occurrences of 10 ^ 1 -> Add 102 0s

Has hundred + 2 occurrences of 10 (2*5) -> Add 102 0s
Has ten + 2 occurrences of 20 * 50 -> Add 10 0s
.... so basically double the top one
= 230 NOPE, GET REKD, now what?
OR

COUNT 5s?!?!
COUNT 50s?!?!
SO ON?
WHAT ABOUT 25 or 250, you so dumb.

1024 / 5 = 204
1024 / 50 = 20
1024 / 500 = 2
YEP doesn't work
....

1024 / 5 = 204
204 / 5 = 40
40 / 5 = 8
8 / 5 = 1
Total: 253 WHY, WHY DOES THIS WORK, OH GOD

204 / 5 -> 1024/25
40 / 5 -> 1024/125
8 / 5 -> 1024/625
THIS IS WHY, LOL
that 25 can combine with a 2 (abundant)
your next largest 0 causing number wasn't 50 in the 100s it was 25.
So 100 has four 25s. SOLVED

'''
import sys

num = int(input())
i = 0
while i < num:
    x = int(input())
    count = 0
    while x > 0:
        x = int(x/5)
        count += x
    print(count)
    i += 1



