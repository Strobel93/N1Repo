# https://codeforces.com/problemset/problem/2/C
# Inputs:
centre_coordinates = [[0,0],[60,0],[30,30]]

def list_element_average(list_to_check: list, inner_list_index: int) -> float:
    sublist = [subelement_list[inner_list_index] for subelement_list in list_to_check]
    return sum(sublist) / len(sublist)

x = list_element_average(centre_coordinates,0)
y = list_element_average(centre_coordinates,1)    
