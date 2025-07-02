import math
import sys

DEBUG = False

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = int(input())
p_1 = list( map ( int, input().split() ) )
used = [False] * len(p_1)
sum1 = 0
for i in range(n):
    p_2 = list (map ( int, input().split() ))
    for j in range(5):
        if used[j] == True:
            continue
        for k in p_2:
            drint("Compre", p_1[j], k)
            if p_1[j] == k:
                drint("matched")
                used[j] = True
                sum1 += 1
print(sum1)



