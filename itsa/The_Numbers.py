import math
import sys

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


# @return list[int]
def find_all_value_idx(list_1d, target):
    return [idx for idx, val in enumerate(list_1d) if val == target]

# @return list[val_t]
def find_all_value_val(list_1d, target):
    return [val for idx, val in enumerate(list_1d) if val == target]


# @return list_1d[str]
def get_num_len (len1, str1):
    s = 0
    e = len(str1) - 1
    ret = []
    while s + len1 - 1 <= e:
        ret.append( str1[s:s+len1] )
        s += 1
    return ret


# n = int(input())
# for i in range(n):
a, b = map(int, input().split())
list_1d = get_num_len(len(str(a)), str(b))
ans_1d = find_all_value_idx(map(int, list_1d), a)
print(len(ans_1d))






