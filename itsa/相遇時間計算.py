import math

num = int(input())

OTHER_SPD = 30*2.54 / 100
MY_SPD = 1

sec = num / (MY_SPD - OTHER_SPD)

print(math.ceil(sec))
