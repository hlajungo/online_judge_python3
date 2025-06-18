num = int (input())

def dist(x1, y1, x2, y2 ) -> float:
    return math.sqrt( pow( x1 - x2, 2) + pow(y1 - y2, 2)  )


def to_base(n: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result


def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n) -> bool:
    if n == 0 or n == 1: # On math define, (0,1) aren't prime
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(num: int) -> list:
    i = 2
    count = 0
    list1 = []
    while num != count:
        if is_prime(i):
            list1.append(i)
            count += 1
        i += 1
    return list1


def swap(x, y):
    return y, x


def factorial (num: int) -> int:
    if num == 0:
        return 1
    ret = 1
    for i in range(2,num+1):
        ret *= i
    return ret

def bissextile_year(n: int) -> bool:
    if n % 400 == 0:
        return True
    elif n% 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

def partition_2_min_diff(nums: list) -> int:
    total = sum(nums)
    n = len(nums)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):·
            dp[j] = dp[j] or dp[j - num]

    for i in range(target, -1, -1):
        if dp[i]:
            return total - 2 * i


def list_to_int (list1: list) -> int:
    t = 1
    max_ = 0
    for i in list1:
        max_ += t * i
        t *= 10
    return list1

def reverse (num: int) -> int:
    return int(str(num)[::-1])

def transpose_2d(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]

# [in,data] str1
# [in,control] len1
# [ret,] list
# 把 str1 的長度 len1 的子字串組成 list 返回
# ex: get_num_len (2, "1234") -> ["12", "23", "34"]
def get_num_len (len1, str1):
    s = 0
    e = len(str1) - 1
    ret = []
    while s + len1 - 1 <= e:
        ret.append( str1[s:s+len1] )
        s += 1
    return ret


