import math

# a, b, c = map(int, (input().split()))

nums=[]

n = int(input())
for i in range(n):
    nums.append(int(input()))

average = sum(nums) / len(nums)

a1=0
a2=0
for i in nums:
    if i >= 900:
        a1+=1
    if i > 600 and i <= 700:
        a2+=1


print(max(nums), a1, a2, round(average, 1), sep='\n')

