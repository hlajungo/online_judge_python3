import math
DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = int(input())
for i in range(n):
    num = int(input())
    if num < 18.5:
        print("體重過輕")
    elif 18.5 <= num and num < 24:
        print("正常")
    elif 24 <= num and num < 28:
        print("體重過重")
    elif num >= 28:
        print("肥胖")


