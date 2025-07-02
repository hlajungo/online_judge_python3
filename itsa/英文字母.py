DEBUG = True

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

vowels = "aeiouAEIOU"

a = input()

tri = False
for i in vowels:
    if a[0] == i:
        print("母音")
        tri = True
        break
if tri == False:
    print("子音")
