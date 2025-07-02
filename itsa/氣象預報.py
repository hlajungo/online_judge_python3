import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = int(input())
for i in range(n):
    num = int(input())
    if (0 <= num and num <= 60 and num > 37) \
    or (70 <= num and num <= 500 and num > 150):
        print("避免外出")
    else:
        print("可依需要待在戶外")

