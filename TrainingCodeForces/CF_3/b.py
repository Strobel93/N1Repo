# https://codeforces.com/problemset/problem/3/b
# Inputs:
truck_volumn = 5 #1,3,5
available_verhicles = [[1,2],[2,7],[1,3]] # required capacity + carryload

#Find most efficient ones (carryload/required capacity), if efficiency is equal, chose lighter first
#Add current index until not enough space any more, move onto the the next
def capacity_func(volume: int, vehice_list: list):
    efficieny_sorted_list = sorted(available_verhicles, key=lambda x: (x[1] / x[0], x), reverse = True)
    total_capacity = 0
    for vehicle in efficieny_sorted_list:       
        while volume - vehicle[0] >= 0:
            total_capacity += vehicle[1]         
            volume -= vehicle[0]
            print(vehicle,total_capacity)

capacity_func(truck_volumn,available_verhicles)


