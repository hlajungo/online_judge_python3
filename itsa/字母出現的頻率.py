import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

n = input()

list1 = [0 for _ in range(26)]

for ch in n:
    if 'a' <= ch <= 'z':
        idx = ord(ch) - ord('a')
        list1[idx] += 1

    if  'A' <= ch <= 'Z':
        idx = ord(ch) - ord('A')
        list1[idx] += 1

print(" ".join(map(str, list1)))

