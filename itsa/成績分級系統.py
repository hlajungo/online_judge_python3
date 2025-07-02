import math
import sys

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


n = int(input())
# coin_1d = list(map(int, input().split() ) )
list_1d = []
for i in range(n):
    list_1d.append(int(input()))

tier_1 = list(filter(lambda x: 100 >= x and x >= 90, list_1d))
tier_2 = list(filter(lambda x: 89 >= x and x >= 80, list_1d))
tier_3 = list(filter(lambda x: 79 >= x and x >= 70, list_1d))
tier_4 = list(filter(lambda x: 69 >= x and x >= 60, list_1d))
tier_5 = list(filter(lambda x: 59 >= x and x >= 0, list_1d))
print("優等",len(tier_1))
print("甲等",len(tier_2))
print("乙等",len(tier_3))
print("丙等",len(tier_4))
print("不及格",len(tier_5))





