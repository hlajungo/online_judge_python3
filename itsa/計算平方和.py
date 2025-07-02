import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

nums = list( map ( int, input().split() ) )
print (sum ( i ** 2 for i in nums ))

