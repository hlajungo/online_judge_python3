-------------- start python version
def ava_max (mat: list[list[int]], stat: list[list[bool]]) -> tuple:
這種內建表達，在 python-3.9+ 才有


--------- start basic operating
a // b
整數除法

a / b
浮點數除法

a ** 2
平方

bin(num) -> str
bin(num & 0b11111111) -> str
hex(num) -> str
進制轉換的方法

from decimal import Decimal, ROUND_HALF_UP
(area.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
確保精度正確

--------- end basic operating






--------------- start math
math.ceil (a)
math.floor (a)
math.gcd(a,b)

mat = list(zip(*mat))
mat = [list(row) for row in zip(*matrix)]
transpose 的方法


--------------- end math


------------------ start logic

for _ in range(0, 100, 1):
0 到 99 的迴圈

for _ in (100,0,-1):
100 到 1 的迴圈

for idx, i in enumerate(t):
想要同時得到索引和值

------------------ end logic



---------- start io
a, b = input().split()
把輸入放到變數的方法，',' 和 'b' 間的空格是必須的


f_str = f"{VARIABLE:.2f}"
使用 f-string 強制小數補 2 個 0 

---------- end io




---------------------------- start map_object and generator_object
這兩個東西是一次性迭代器，作為參數時，可以用 for 進行存取，不能用 [] 存取，只能存取一次。

def f(gen):
    for val in gen:
        print(val)

map (type, list) -> <map object>
把 list 中每個元素進行 type 轉換

list(<class 'map'>) -> list
list(<class 'generator'>) -> list

----------------------------- end map_object and generator_object




----- start generator_object
gen = (x * 2 for x in range(3))
print(gen)         # <generator object ...>
print(next(gen))   # 0
print(next(gen))   # 2
print(next(gen))   # 4
generator_object 的延遲運算性，允許把過程掰開來，一個一個運作，以在中間支持更複雜的操作

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
yield 用來產生 generator_object

----- end generator_object





-------------- start XXX Comprehension (推導式)
"A for B in C"  是一個語法糖，稱為 XXX Comprehension。
A 是表達式，B 是變量，能在 A 使用變量 B，C 是變量生成範圍。

這個語法糖可用於生成以下四種物件
list1 = [A for B in C]
set1 = {A for B in C}
dict1 = {A: B for C in D}
generator object (A for B in C)



以下是範例

list1 = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
取得平方數組

set1 = {ch for ch in "hello"}
# {'h', 'e', 'l', 'o'}
唯一化字串

dict1 = {ch: ord(ch) for ch in 'abc'} # {'a': 97, 'b': 98, 'c': 99}
建立 "字符 - ascii" 映射

str1 = " ".join(str(x).zfill(3) for x in [1, 2, 3, 4, 5]))
# "001 002 003 004 005"
在字串處理時，連帶處理補 0 操作

-------------- end XXX Comprehension (推導式)






-----------------------------------------start list

list1 = [0 for _ in range(26)]
list1 = [0] * 26
C++ 的 vector list1(26)


mat = [[0] * 26] * 26
錯誤的寫法，會產生 26 個指向相同記憶體位置的 list，內容為 [0] * 26。
任何修改會同時修改所有 list

mat = [[0 for i in 26] for j in 26]
mat = [[0] * 26 for _ in 26]
正確的寫法。

-----------------------------------------end list






------------------------------------------ start str slice

str[A:B:C] -> str
String slice from A to B-1，C is step。
-A, -B, -C 代表反著來。

[:i]  前 i 個, i = range (1, len(X)+1 )
[-i:] 後 i 個, i = range (1, len(X)+1 )

0123456

str[:3] 012 (First 3)
s[-3:] 456 (Last 3)
str[3:] 3456 (Remove first 3)
s[:-3] 0123 (Remove last 3)
str[::-1] 6543210 (Reverse)

------------------------------------------- end str slice







----------- start str func
str.zfill(n: int) -> str
前方補 0

"{}XXX".format (VAR) -> str
把 VAR 丟到 {} 組合成字符串

("*" * 100 + '\n' ) * 100
str 的整數乘法與加法，產生 100 * 100 的 '*' 方塊

str.split() -> list_str

str.split(",") -> list_str


",".join(list) -> str
",".join(map(str, list)) -> str
",".join(A for B in C ) -> str
把一個物件之間元素用","連起來，成為一個字串

------------- end str func




--------------------------------------------start char

ord('c')
python 的字符是字符，不是數字，使用 ord 轉數字

if  'A' <= ch <= 'Z':
字符之間的比較仍通過 ascii

for ch in n:
字串的遍歷

--------------------------------------------end char
