import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# for i in range(n):
    # num = int(input())
n = input()

if sum (int(i) ** 3 for i in n) == int(n):
    print("YES")
else:
    print("NO")


