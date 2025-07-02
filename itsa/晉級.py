import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


n = int(input())

pass1 = 0

for i in range(n):
    subject, score = input().split()
    score = int(score)
    if score >= 60:
        print (subject)
        pass1 += 1

if pass1 >= math.ceil(n/2):
    print("晉級")
else:
    print("失敗")


