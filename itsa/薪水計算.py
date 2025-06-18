wt, sa = map(int, input().split(" "))


price = 0

if wt >= 121:
    l_p = wt - 120
    price += l_p * sa * 1.66
    price += 60 * sa * 1.33
    price += 60 * sa

if wt >= 61 and wt <= 120:
    l_p = wt - 60
    price += l_p * sa * 1.33
    price += 60 * sa

if wt <= 60:
    price += wt * sa

print(price)




