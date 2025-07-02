import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = input()
nums = list( map ( int, input().split() ) )
s, e = map ( int, input().split() )

print( sum(nums[s-1:e]) ) # e = e - 1 + 1

