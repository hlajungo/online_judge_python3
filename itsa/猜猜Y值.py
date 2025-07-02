import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


n = int(input())
for i in range(n):
    num = int(input())
    if 50 < num and num <= 70:
        print(num)
    else:
        print(100)
