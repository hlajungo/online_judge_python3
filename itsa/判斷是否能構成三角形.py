import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

nums = list(map(int, (input().split()) ) )


nums.sort()
if nums[0] + nums[1] > nums[2]:
    print("fit")
else:
    print("unfit")



