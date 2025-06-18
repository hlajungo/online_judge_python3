
a, b = map(int, input().split())

bmi = a / ((b /100) ** 2)
f_bmi = f"{bmi:.2f}"

print ( f_bmi )
