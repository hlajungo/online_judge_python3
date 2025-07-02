import math
import sys

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

a = input()
b = input()
# for i in range(n):
# a, b = map(int, input().split())
print("YES") if a in b else print("NO")




