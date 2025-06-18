import math


def factorial (num: int) -> int:
    ret = 1
    for i in range(2,num+1):
        ret *= i
    return ret


# a, b = map(int, (input().split()))
n = int(input())
for i in range(n):
    num = int(input())
    print (factorial(num))
    


