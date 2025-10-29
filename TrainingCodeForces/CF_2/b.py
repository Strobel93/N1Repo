# https://codeforces.com/problemset/problem/2/B
# Inputs:
n = 3 # Matrix dimension


# # Only for Visualisation
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][0]) # Start
# print(matrix[0][1])
# print(matrix[2][2]) # End

# Find all possible ways from start to end, only being allowed to go down or right
valid_path_list = []
start_pos = [0,0]
current_pos_list = [[start_pos,start_pos]] #[[CurrentCheck],[PathHistory]]
# print(current_pos_list[0][0])



# Does Position to right/down exist?
# Is within boundaries of matrix?
def check_movement_exist(current_pos_right: int, current_pos_down: int, dimension_size: int) -> bool:
    right = True if current_pos_right + 1  <= dimension_size else False #Dimensionsize is N, but Index is N-1
    down = True if current_pos_down + 1  <= dimension_size else False #Dimensionsize is N, but Index is N-1
    return right, down
# print(check_movement_exist(0,0,3))
# print(check_movement_exist(3,2,3))
# print(check_movement_exist(3,3,3))

# For each step, add all current whole paths to list that are allowed
# in the end, only those are valid, whos last element in list is the matrix end
# loop until there are no more elements in current_pos_list whos result is FALSE, FALSE
while current_pos_list:
    current_check = current_pos_list.pop()
    current_right_coordinate = current_check[0][0]
    current_down_coordinate = current_check[0][1]
    right, down = check_movement_exist(current_right_coordinate, current_down_coordinate, n)
    # Add History to list if current position is final step
    if current_right_coordinate == n -1 and current_down_coordinate == n -1:
        valid_path_list.append(current_check[1])
    # Add valid new checkpoints + [current path history + new step]
    # only right 
    if right and not down:
        current_pos_list.append([[current_right_coordinate+1, current_down_coordinate], current_check[1]+[current_right_coordinate + 1, current_down_coordinate]])
    # only left
    if down and not right:
        current_pos_list.append([[current_right_coordinate, current_down_coordinate + 1],current_check[1]+[current_right_coordinate, current_down_coordinate + 1]])
    # left and right
    if down and right:
        current_pos_list.append([[current_right_coordinate+1, current_down_coordinate], current_check[1]+[current_right_coordinate + 1, current_down_coordinate]])
        current_pos_list.append([[current_right_coordinate, current_down_coordinate + 1],current_check[1]+[current_right_coordinate, current_down_coordinate + 1]])

for path in valid_path_list:
    print(path)