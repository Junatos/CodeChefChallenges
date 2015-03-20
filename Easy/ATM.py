__author__ = 'arjunkumar'

# Solution to http://www.codechef.com/problems/HS08TEST

import sys

# withdraw, init_bal = [int(x) for x in input().split()]
terrible_input_split = input().split()
withdraw = int(terrible_input_split[0])
init_bal = float(terrible_input_split[1])

final_withdraw = withdraw + 0.50

if final_withdraw < init_bal and withdraw % 5 == 0:
    print(init_bal - final_withdraw)
else:
    print(init_bal)
