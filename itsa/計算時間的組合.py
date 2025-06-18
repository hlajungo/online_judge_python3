import math
num = int (input ())

sec = num % 60
min_ = (num // 60) % 60
hour = (num // 60 // 60) % 24
day = num // ( 60 * 60 * 24 )

print('{} days'.format(day))
print('{} hours'.format(hour))
print('{} minutes'.format(min_))
print('{} seconds'.format(sec))

