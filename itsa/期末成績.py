import math
import sys

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


n = int(input())
# coin_1d = list(map(int, input().split() ) )
list_1d = []
for i in range(n):
    list_1d.append(int(input()))



print(f"Max:{max(list_1d)}")
print(f"Min:{min(list_1d)}")
print(f"Average:{ round( sum(list_1d) / len(list_1d) , 1)}")
print(f"Pass:{len( list( filter(lambda x: x>= 60  ,list_1d) ) )}")




