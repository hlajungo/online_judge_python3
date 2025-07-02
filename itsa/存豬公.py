import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

a = int(input())
b = int(input())

sum = 0

for i in range(b):
    sum += a
    a *= 2

print (f"第{b}天共存{sum}元")


