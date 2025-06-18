h1, m1 = map(int, input().split(" "))
h2, m2 = map(int, input().split(" "))

m_diff = h2*60 + m2 - h1*60 - m1

price = 0

if m_diff >= 240:
    l_p = m_diff - 240
    price += (l_p // 30) * 60
    price += 30 * 4
    price += 40 * 4

if m_diff >= 120 and m_diff < 240:
    l_p = m_diff - 120
    price += (l_p // 30) * 40
    price += 30 * 4

if m_diff < 120:
    price += (m_diff // 30) * 30

print(price)




