import math

def is_prime(n):
    if n == 0 or n == 1: # On math define, (0,1) aren't prime
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input())

num-=1
while is_prime(num) == False:
    num -=1

print(num)

