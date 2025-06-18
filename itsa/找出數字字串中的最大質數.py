import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# col= map(int, input().split(" "))


# 123
# s=0, e=2

def get_num_len (len1, str1):
    s = 0
    e = len(str1) - 1
    ret = []
    while s + len1 - 1 <= e:
        ret.append( str1[s:s+len1] )
        s += 1
    return ret

def is_prime(n) -> bool:
    if n == 0 or n == 1: # On math define, (0,1) aren't prime
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = input()


found = False
for i in range(len(n)-1,-1,-1):
    list1 = get_num_len(i+1, n )
    primes = []
    for j in list1:
        if is_prime(int(j)):
            primes.append(int(j))
            found = True
    if found:
        print (max(primes))
        break

if found == False:
    print ("No prime found")
