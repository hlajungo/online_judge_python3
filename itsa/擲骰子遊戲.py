import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

nums = list (map(int, (input().split()) ) )

sum1 = sum(nums)

if sum1 > 9:
    print(sum1, "H")
else:
    print(sum1, "L")
