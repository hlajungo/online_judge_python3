import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

"""
1432219, 3
s 1
s 14
s 13 b 2
s 12 b 1
s 121 b 0
s 1219

非常的驚豔
對於 14,13,12 的更改，因為是百位數，所以更改會更小。9 在最後一位數，所以影響不大。
我們要尋求當前位數可能的最小值
"""

# @param a str
# @param b int
def remove_digit_min(a, b):
    stack = []
    for digit in a:
        while b > 0 and stack and stack[-1] > digit:
            stack.pop()
            b -= 1
        stack.append(digit)

    # 若還沒刪夠，從後面刪
    while b > 0:
        stack.pop()
        b -= 1

    result = "".join(stack).lstrip("0")
    return result if result else "0"

# ex:
# 1432219, 3 -> 1219

a, b = input().split(",")

print( remove_digit_min(a, int(b)) )










