import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# col= map(int, input().split(" "))

n = int(input())
nums = list( map(int, input().split(" ")) )
ret = [0] * len(nums)
for idx, i in enumerate(nums):
    if (idx == 0):
        ret[0] = nums[0]
        continue
    ret[idx] = i - nums[idx-1]

print(" ".join(str(i) for i in ret) )


