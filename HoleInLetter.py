__author__ = 'arjunkumar'

# solution to http://www.codechef.com/problems/HOLES

import sys

num = int(input())
i = 0

while i < num:
    word = input()
    count = 0
    dict_holes = {'A': 0, 'D': 0, 'O': 0, 'P': 0, 'R': 0, 'Q': 0, 'B': 0}
    for ch in list(word):
        try:
            dict_holes[ch] += 1
        except:
            pass

    count += dict_holes['A'] + dict_holes['D'] + dict_holes['O'] + dict_holes['P'] + dict_holes['R'] + dict_holes['Q'] + (dict_holes['B'] * 2)
    print(count)
    i += 1
