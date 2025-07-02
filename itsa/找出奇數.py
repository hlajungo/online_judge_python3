import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# for i in range(n):
    # num = int(input())
n = int(input())

ans = []
for i in range(1,n+1):
    if i %2 == 1:
        ans.append(i)

print(" ".join(map(str, ans)))

