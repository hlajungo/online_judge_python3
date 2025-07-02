import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# for i in range(n):
    # num = int(input())

n = int(input())
if n == 1:
    print("Person")
elif n == 2:
    print("Fairy")
else:
    print("Dwarf")
