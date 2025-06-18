import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

n = input()

list1 = list(map(int, input().split()) )

count =0
for i in range(1, len(list1)+1):

    sum_l = list1[:i]
    sum_r = list1[-i:]
    # print (sum_l)
    # print (sum_r,"---")
    if sum(sum_l) == sum(sum_r):
        count += 1

print (count)


