import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input ().split() )
print (math.gcd(a, b))
# print (gcd(a, b))
