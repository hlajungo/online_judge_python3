import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# col= map(int, input().split(" "))

# 根據兩者好感度，進行匹配，每次給出當前最好，並操作 stat 以確保下次也是給出最好
# 有點像西洋棋的全車放置
# mat 兩者好感度
# stat 這元素是否可選擇
# ret 當前最優配對
def ava_max (mat: list[list[int]], stat: list[list[bool]]) -> tuple:
    max_2d = 0
    tar_ij = (-1,-1)
    # find the max of array
    for i,a in enumerate (mat):
        for j,b in enumerate(a): # b == list[i][j]?
            if stat[i][j] == False:
                if b > max_2d:
                    tar_ij = (i,j)
                    max_2d = max(b, max_2d)

    # set the stat
    i, j = tar_ij
    # print ("max",max_2d, i, j)
    for si in range(len(stat)):
        stat[i][si] = True
        stat[si][j] = True
    return (i,j)

col = int(input())

mat = [[0] * col for _ in range(col)]
mat_bool = [[False] * col for _ in range(col)]

for i in range(col):
    mat[i] = list(map(int, input().split(" ")))

for i in range(col):
    i, j = ava_max(mat, mat_bool)
    print("boy",i+1,"pair with girl", j+1)



# for i in mat:
    # print(" ".join(str(j) for j in i))



