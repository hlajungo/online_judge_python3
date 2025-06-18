import math

def is_prime(n):
    if n == 0 or n == 1: # On math define, (0,1) aren't prime
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

ans = []
n = int(input())
if n%2 == 0:
    ans.append("even")
else:
    ans.append("odd")

if is_prime(n):
    ans.append("prime")

print(" ".join(ans) )

