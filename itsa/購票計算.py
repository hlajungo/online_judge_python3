import math

num = int (input())

print ("NT10=", math.floor (num / 10), sep="")
num %= 10

print ("NT5=", math.floor (num / 5), sep="")
num %= 5

print ("NT1=", num, sep="")

