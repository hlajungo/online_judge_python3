import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = input()
strs = input().split()
fav = input()


sum1 = 0
is_fav = False
for str1 in strs:
    is_fav = True
    for ch in fav:
        if not ch in str1: # Not fav
            is_fav = False
            break
    if is_fav == True:
        sum1 += 1
print (sum1)

