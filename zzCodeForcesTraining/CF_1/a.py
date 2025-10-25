# https://codeforces.com/problemset/problem/1/A
# Inputs:
    # n: Length
    # w: with
    # a: length & witdth of squares to cover n & w
import math
n = 6
w = 6
a = 4

def cf_1(n: int, w: int, a: int):
    length_min = math.ceil(n/a)
    width_min = math.ceil(w/a)
    return length_min * width_min

print(cf_1(n,w,a))

