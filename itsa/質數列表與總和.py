import math

def is_prime(n):
    if n == 0 or n == 1: # On math define, (0,1) aren't prime
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(num: int) -> list:
    i = 2
    count = 0
    list1 = []
    while num != count:
        if is_prime(i):
            list1.append(i)
            count += 1
        i += 1
    return list1




# a, b = map(int, (input().split()))

# n = int(input())
# for i in range(n):

num = int(input())
list1 = prime_list(num)
sum1 = sum (list1)

print(list1[0], end="")
for i in range(1,len(list1)):
    print(",{}".format(list1[i]), end="")
print()
print(sum1)


