import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

eng_1d="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
moose_1d = [".-", "-...", "-.-.", "-..", ".",
 "..-.", "--.", "....", "..", ".---",
 "-.-",".-..","--","-.","---",
 ".--.","--.-",".-.","...","-",
 "..-","...-",".--","-..-","-.--","--.."]
dict_1d = {}
for idx, ch in enumerate(eng_1d):
    dict_1d[moose_1d[idx]] = ch

list_1d = list(input().split())
# for i in range(n):
    # a, b = map(int, input().split())

print("".join(dict_1d[x] for x in list_1d ))





