num = int(input())

price = 0
if num < 800:
    price = num*0.9
elif num >= 800 and num < 1500:
    price = num * 0.9 * 0.9
else:
    price = num * 0.79 * 0.9

print(f"{price:.1f}")

