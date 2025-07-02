import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

a, b = input().split()

def flip_2d(list_2d):
    new_list_2d = []
    for list_1d in list_2d[::-1]:
        new_list_2d.append(list_1d)
    return new_list_2d

def transpose_2d(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def rotate_left_2d(list_2d):
    return flip_2d( transpose_2d(list_2d) )

def rotate_right_2d (list_2d):
    return transpose_2d(flip_2d(list_2d))


def gen_square_2d(s, len1):
    list_2d = []
    for i in range(len1):
        list_1d = []
        for j in range(s, s + len1):
            list_1d.append(i*len1 + j)
        list_2d.append(list_1d)
    return list_2d

list_2d = gen_square_2d(1, int(a))
if b == "L":
    for list_1d in rotate_left_2d(list_2d):
        print(" ".join(map(str, list_1d)) )
elif b == "R":
    for list_1d in rotate_right_2d(list_2d):
        print(" ".join(map(str, list_1d)) )
else:
    for list_1d in flip_2d(list_2d):
        print(" ".join(map(str, list_1d)) )











