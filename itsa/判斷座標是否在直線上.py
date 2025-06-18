import math

a, b, c = map(int, (input().split()))
x1, y1 = map(int, (input().split()))

if a*x1 + b*y1 + c == 0:
    print("YES")
else:
    print("NO")

# n = int(input())
# for i in range(n):


