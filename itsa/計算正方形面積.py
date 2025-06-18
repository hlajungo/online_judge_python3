from decimal import Decimal, ROUND_HALF_UP

n = int(input())
for i in range(n) :
    num = Decimal(input())
    area = num*num
    print(area.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

# python 的 float 不是精確的 0.25 可能會是 0.250000000000000000003
# 精確的數字要使用 decimal，他們保證 0.25 是 0.25

