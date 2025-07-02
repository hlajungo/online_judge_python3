import math
import sys

DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

a, b = map(int, (input().split()) )

def dist(x1, y1, x2, y2 ) -> float:
    return math.sqrt( pow( x1 - x2, 2) + pow(y1 - y2, 2)  )


def is_inside_circle(c_x, c_y, c_len, x, y):
    if dist (c_x, c_y, x, y) <= c_len:
        return True
    else:
        return False


if is_inside_circle(0, 0, 100, a, b) == False:
    print("outside")
else:
    print("inside")
