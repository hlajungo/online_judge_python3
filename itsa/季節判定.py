import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# for i in range(n):
    # num = int(input())

n = int(input())
if 3 <= n and n <= 5:
    print("Spring")
elif 6 <= n and n <= 8:
    print("Summer")
elif 9 <= n and n <= 11:
    print("Autumn")
else:
    print("Winter")
