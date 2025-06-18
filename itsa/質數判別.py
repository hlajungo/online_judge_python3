import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

n = int(input())

def is_prime(n):
    if n == 0 or n == 1: # On math define, (0,1) aren't prime
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print("YES")
else:
    print("NO")
