str1 = input()

i = len(str1) - 1

print(str1[i], end="")
i -= 1

while i >= 0:
    print("," + str1[i], end="")
    i -= 1

# '\n' use at default, use `end=""` to remove '\n'
print()
