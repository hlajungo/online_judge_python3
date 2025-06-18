import math

n = int (input())

for i in range(n) :
    # tuple unpacking for make list to variable
    a, b = map(int, input().split() )
    print ( pow ( (a+b), 2) )


