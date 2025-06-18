import math

def swap(x, y):
    return y, x

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = swap(a, b)
    sum = (1 + b) * b // 2 - (a - 1) * a // 2
    print(sum)


