import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# list_1d = list(map(int, input().split()) )
n = int(input())
list_1d = []
for i in range(n):
    list_1d.append( int(input()) )

list_1d.sort(reverse=True)

print("".join(map(str, list_1d)) )









