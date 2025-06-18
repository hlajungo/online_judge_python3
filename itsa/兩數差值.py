import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# n = input()

list1 = list(map(int, input().split(',')) )

list1.sort()

t = 1
max_ = 0
for i in list1:
    max_ += t * i
    t *= 10

print(max_ - int(str(max_)[::-1]))


