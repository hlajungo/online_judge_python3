import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = int(input())
for i in range(n):
    num = int(input())
    if 90 <= num and num <= 100:
        print("優等")
    elif 80 <= num and num <= 89:
        print("甲等")
    elif 70 <= num and num <= 79:
        print("乙等")
    elif 60 <= num and num <= 69:
        print("丙等")
    else:
        print("不及格")

