import math

# a, b = map(int, (input().split()))

# n = int(input())
# for i in range(n):

num = int(input())
if num <= 9:
    print(100*num)
elif num >= 100:
    print(70*num)
elif num >= 30:
    print(80*num)
elif num >= 10:
    print(90*num)


