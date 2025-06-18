import math

strs = input().split()
# nums = list (map (int, nums))
a=strs[0]
ai=int(strs[0])
b=strs[1]
bi=int(strs[1])
print (a+"+"+b+"="+str(ai+bi))
print (a+"*"+b+"="+str(ai*bi))
print (a+"-"+b+"="+str(ai-bi))

# bi might <0
div = math.floor(ai/bi)
if bi < 0:
    div = math.ceil(ai/bi)

# mod might <0, make it >0
mod = ai%bi
if mod <0:
    mod -= bi

print (a+"/"+b+"="+str(div)+"..."+str(mod))
# X.ceil, X.floor, X=math

