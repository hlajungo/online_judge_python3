import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# n = input()

list1 = list(map(int, input().split()) )

t = [0] * 100

for i in list1:
    t[i]+=1

tr = 0
for i in t:
    if i == 2:
        print(tr)
    tr+=1



