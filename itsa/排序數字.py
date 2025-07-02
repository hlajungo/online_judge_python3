import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = input()
list_1d = list(map(int, input().split()) )
list_1d.append(int(input()))

list_1d.sort()
print(",".join(map(str, list_1d)))









