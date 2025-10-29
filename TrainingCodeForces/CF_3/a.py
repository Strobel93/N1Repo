# https://codeforces.com/problemset/problem/3/A
# Inputs:

#Chessboard:
    #8x8
    #X=a-h
    #Y=1-8
chessboard_start = 'a8'
chessboard_end = 'd6'#c5,h1,d6

alpha_numerical_mapping = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

#Check is lower or higher, move diagonal as long as height <> height
#Move straight after
def find_moves(start:str,end:str):
    start = [alpha_numerical_mapping[start[0]],int(start[1])]
    end = [alpha_numerical_mapping[end[0]],int(end[1])]
 
    #Steps
    number_of_steps = max(abs(start[0]-end[0]),abs(start[1]-end[1]))
    number_diagonal = min(abs(start[0]-end[0]),abs(start[1]-end[1]))

    #Directions
    up_or_down = 'Down' if start[1] > end[1] else 'Up'
    left_or_right = 'Left' if start[0] > end[0] else 'Right'
    final_direction = left_or_right if abs(start[0]-end[0]) > abs(start[1]-end[1]) else up_or_down

    #Move
    for i in range(number_of_steps):
       movement = ''
       movement += up_or_down + ' ' + left_or_right if i < number_diagonal else final_direction
       print(movement)


find_moves(chessboard_start,chessboard_end)
