# https://codeforces.com/problemset/problem/2/A
# Inputs:
import time

game_scores_1 = [["mike", 3], ["andrew", 5], ["mike", 2]]
game_scores_2 = [["andrew", 3], ["andrew", 2], ["mike", 5]]
game_scores_3 = [["andrew", 3], ["andrew", 2], ["mike", 5], ["mike", 5], ["mike", 5], ["andrew", 2]]

# Name,CurrentScore,IsFirstToReachScore
def calc_winner(game_score_list: list) -> list:
    score_list = {}
    winner = ''
    for round_Score in game_score_list:
        # Insert New Scores
        if round_Score[0] not in score_list.keys():
            winner =  winner if any(value >= round_Score[1] for value in score_list.values()) else round_Score[0]
            score_list[round_Score[0]] = round_Score[1]
        # update existing scores 
        else:
            winner = winner if any(value >= (round_Score[1] + score_list[round_Score[0]]) for value in score_list.values()) else round_Score[0]
            score_list[round_Score[0]] = round_Score[1] + score_list[round_Score[0]]
    return score_list,winner


print(calc_winner(game_scores_1))       
print(calc_winner(game_scores_2))       
print(calc_winner(game_scores_3))       

