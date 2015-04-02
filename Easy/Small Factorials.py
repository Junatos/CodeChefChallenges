__author__ = 'Jun'

# solution for http://www.codechef.com/problems/FCTRL2

import math

num_of_input = int(input())

i = 0

while i < num_of_input:
    num = int(input())
    print(math.factorial(num))
    i += 1

'''
yes I cheated, I used Python's math factorial function. It uses a binary split divide and conquer factorial which
was too hard for me to understand. More here:
https://hg.python.org/cpython/file/7937aa6b7e92/Modules/mathmodule.c#l1218
http://www.luschny.de/math/factorial/binarysplitfact.html
'''

