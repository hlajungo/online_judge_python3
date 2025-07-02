import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# for i in range(n):
    # num = int(input())
n = int(input())

print("百元", n // 100)
print("十元", (n % 100 // 10) )
print("壹元", (n % 10))


