import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

nums = list(map(int, (input().split()) ) )

def is_triangle(lens):
    lens.sort()
    if lens[0] + lens[1] > lens[2]:
        return True
    else:
        return False


if not is_triangle(nums):
    print("Not Triangle")
    sys.exit(0)

stat = nums[0] ** 2 + nums[1] ** 2 - nums[2] ** 2
if stat == 0:
    print("Right Triangle")
elif stat > 0:
    print("Acute Triangle")
else:
    print("Obtuse Triangle")
