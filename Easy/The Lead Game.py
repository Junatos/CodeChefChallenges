__author__ = 'arjunkumar'

# solution to http://www.codechef.com/problems/TLG

n = int(input())
max_lead = 0
max_lead_player = 1
player_1_total_score = 0
player_2_total_score = 0

for i in range(n):
    player_1_score, player_2_score = map(int, input().split())
    player_1_total_score += player_1_score
    player_2_total_score += player_2_score

    lead = player_1_total_score - player_2_total_score
    abs_lead = abs(lead)
    if max_lead < abs_lead:
        max_lead = abs_lead
        if lead > 0:
            max_lead_player = 1
        else:
            max_lead_player = 2

print(max_lead_player, max_lead, sep=" ")