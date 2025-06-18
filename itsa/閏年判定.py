import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

n = int(input())

if n % 400 == 0:
    print("Bissextile Year")
elif n% 100 == 0:
    print("Common Year")
elif n % 4 == 0:
    print("Bissextile Year")
else:
    print("Common Year")
