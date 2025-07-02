import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = input()
strs = input().split()
strs = strs[::-1]
print( " ".join(strs) )

