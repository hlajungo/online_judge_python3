import math
n = int(input())

for i in range(n):
    num = int(input())
    if num > 31:
        print("Value of more than 31")
        continue
    print (str( pow(2, num)) )


