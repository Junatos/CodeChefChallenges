__author__ = 'arjunkumar'

import sys

n, *scores = map(int, sys.stdin.buffer.read().split())
i = 0
max_lead = 0
max_lead_player = 1
player_1_total_score = 0
player_2_total_score = 0

while i < 2*n:
    player_1_total_score += scores[i]
    player_2_total_score += scores[i + 1]

    lead = player_1_total_score - player_2_total_score
    abs_lead = abs(lead)
    if max_lead < abs_lead:
        max_lead = abs_lead
        if lead > 0:
            max_lead_player = 1
        else:
            max_lead_player = 2

    i += 2

print(max_lead_player, max_lead, sep=" ")

'''
whoa this cut a full 3.2 seconds off the run time.
hooray, this must mean I'm a coding god right?
yes, that's what it means

mainly, input output is such a pain with these competitive programming things
'''