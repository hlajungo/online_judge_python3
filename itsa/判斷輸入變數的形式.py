import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

def is_int(str1):
    nums = "0123456789"
    for ch in str1:
        if not ch in nums:
            return False
    return True

def is_float(str1):
    nums = "0123456789."
    for ch in str1:
        if not ch in nums:
            return False
    return True


n = input()

if is_int(n):
    print("int")
elif is_float(n):
    print("float")
elif len(n) == 1:
    print("char")
else:
    print("string")

