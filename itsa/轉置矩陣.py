import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# n = input()

col, row = map(int, input().split(" "))
mat = [[0]* row for _ in range(col)]

for i in range(col):
    mat[i] = list(map(int, input().split(" ")))

mat = list(zip(*mat))

for i in mat:
    print(" ".join(str(j) for j in i))



