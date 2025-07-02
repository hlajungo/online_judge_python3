import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

nums = list (map(int, (input().split()) ) )
str1 = input()

if str1 == "Asc":
    nums.sort()
    print ( "<".join(map(str, nums)) )
else:
    nums.sort(reverse=True)
    print(">".join(map(str, nums)) )
