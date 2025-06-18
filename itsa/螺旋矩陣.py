import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# n = input()

mlen, b = map(int, input().split(","))

mat = [[0 for i in range(mlen)] for j in range(mlen)]

# Note: itsa 上沒有成功通過，我也是

top = 0
left = 0
right = mlen
down = mlen
x = 0
y = 0
# 0 right 1 down 2 left 3 top
dire = 0
for i in range(mlen * mlen):
    mat[y][x] = i + 1


    # 最右，往下
    if dire == 0 and x == right - 1:
        dire = 1
        top += 1 # 上方多一排
    # 最下，往左
    elif dire == 1 and y == down - 1:
        dire = 2
        right -= 1 # 右方多一排
    # 最左，往上
    elif dire == 2 and x == left:
        dire = 3
        down -= 1 # 下方多一排
    # 最上，往右
    elif dire == 3 and y == top:
        dire = 0
        left += 1 # 左方多一排

    # 移動
    if dire == 0:
        # 右
        x += 1
    elif dire == 1:
        y += 1
    elif dire == 2:
        x -= 1
    elif dire == 3:
        y -= 1

if b == 2:
    mat = list(zip(*mat))

for i in range(mlen):
    print(" ".join(str(x).zfill(3) for x in mat[i]))



