import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = input()
nums = list( map ( int, input().split() ) )
anss =[]
cur_num = 0
for i in nums:
    cur_num += i
    anss.append(cur_num)
print(" ".join(map(str, anss) ) )

