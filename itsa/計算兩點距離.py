import math

def dist(x1, y1, x2, y2 ) -> float:
    return math.sqrt( pow( x1 - x2, 2) + pow(y1 - y2, 2)  )

x1,y1= map(int, (input().split()))
x2,y2= map(int, (input().split()))


print (f"{round( dist(x1, y1, x2, y2), 2):.2f}")
# print (f"{XXXX:.2f}")


