# https://codeforces.com/problemset/problem/3/D
# Inputs:
bracket_list = ['(','?','?',')']

def handle_bracket(bracket: list):
    #it is cheaper to close instead of open, so try close first
    open_count = 0
    for counter, check in enumerate(bracket):
        if check == '(':
            open_count += 1
        if check == ')':
            open_count -= 1
       
        if check == '?':
             bracket[counter] = ')' if open_count > 0 else '('
             open_count = open_count-1 if open_count > 0 else open_count+1
    print(bracket)    

handle_bracket(bracket_list)    