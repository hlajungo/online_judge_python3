import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

print(max(nums))
