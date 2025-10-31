# https://codeforces.com/problemset/problem/3/C
# Inputs:
#  = 
# X = Player 1
# 0 = Player 2
# Decide
    # Whos turn next?
    # Are the moves even legal? 
    # Who whon?
from collections import Counter

tt_0_turn = [
                ['X','0','X'],
                [' ','0',' '],
                [' ','X',' ']
]
#Illegal, 2 winns
ttt_illegal = [
                ['0','X','X'],
                ['0','X','X'],
                ['X','X','X']
]
ttt_x_win = [
                ['0',' ','X'],
                ['0',' ','X'],
                [' ',' ','X']
]
def check_line(flattend_dictionary: dict,index_list: list) -> str:
    winning_player = ''
    list = [flattend_dictionary[index_list[0]],flattend_dictionary[index_list[1]],flattend_dictionary[index_list[2]]]
    if all(x == 'X' for x in list):
        return 'X'
    if all(x == '0' for x in list):
        return '0'

def ttt_check(ttt_grid: list) -> str:
    game_result = ''
    # Flatten list and add indexes:
    flattend_dictionary = {}
    flattend_list = []
    index = 1
    for sublist in ttt_grid:
        for element in sublist:
            flattend_dictionary[index] = element
            index = index + 1
            flattend_list.append(element)

    index_check_list = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9]]
    winnings_player_x = 0
    winnings_player_0 = 0
    for check in index_check_list:
        winner = check_line(flattend_dictionary,check)
        if winner == 'X':
            winnings_player_x += 1
        if winner == '0':
            winnings_player_0 += 1

    # Valid: player movement count difference is 0 or 1
    # also has to check if not 2 players won
    counts = Counter(flattend_list)
    if (abs(counts['X']-counts['0']) > 1 or winnings_player_x + winnings_player_0 > 1):
        game_result = 'illegal movesets'
        return game_result 
    #Victor?
    game_result = 'X' if winnings_player_x == 1 else '0' if winnings_player_0 == '0' else None
    if game_result == 'X' or game_result == '0':
        return game_result
    #if not whos turn?
    game_result = 'player X next turn' if counts['X'] < counts['0'] else 'player 0 next turn'
    return game_result 
    
    
print('tt_0_turn:   ',ttt_check(tt_0_turn))
print('ttt_illegal: ',ttt_check(ttt_illegal))
print('ttt_x_win:   ',ttt_check(ttt_x_win))

