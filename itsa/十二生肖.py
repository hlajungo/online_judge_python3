import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

chinese_zodiac_1d = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]

num = int(input())
print(chinese_zodiac_1d[(num -4)%12])






