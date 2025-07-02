import math
import sys

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


def average(list_1d):
    return sum(list_1d) / len(list_1d)

n = int(input())
# coin_1d = list(map(int, input().split() ) )
list1_1d = []
list2_1d = []
list3_1d = []
for i in range(n):
    a, b, c = map(int, input().split())
    list1_1d.append(a)
    list2_1d.append(b)
    list3_1d.append(c)

ans = []
ans.append( round((sum(list1_1d) + sum(list2_1d) + sum(list3_1d) ) / ( n*3 ), 1) )
ans.append( round(average(list1_1d), 1) )
ans.append( round(average(list2_1d), 1) )
ans.append( round(average(list3_1d), 1) )

print(" ".join(map(str, ans)) )







