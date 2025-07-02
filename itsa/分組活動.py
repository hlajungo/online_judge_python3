import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = input()
str1 = input()
n = int(input())
ans = []
for i in range( math.ceil(len(str1) / n ) ):
    ans.append( str1[i * n:i * n + n] )


print(" ".join(ans) )
