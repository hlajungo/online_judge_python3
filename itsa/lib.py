##
# General
##

capital_eng_1d="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
moose_1d = [".-", "-...", "-.-.", "-..", ".",
 "..-.", "--.", "....", "..", ".---",
 "-.-",".-..","--","-.","---",
 ".--.","--.-",".-.","...","-",
 "..-","...-",".--","-..-","-.--","--.."]

chinese_zodiac_1d = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]



def swap(x, y):
    return y, x

def bissextile_year(n: int) -> bool:
    if n % 400 == 0:
        return True
    elif n% 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False


##
# list
##

# ex:
# [2, 4, 6] -> 4
def average(list_1d):
    return sum(list_1d) / len(list_1d)


# ex:
# [1,2,3] -> 123
def list_to_int (list1: list) -> int:
    t = 1
    max_ = 0
    for i in list1:
        max_ += t * i
        t *= 10
    return list1


# 組合出最大數
# @ret str
# ex: [14,13,91] -> 911413
def list_to_max(list_1d):
    list_1d.sort(reverse=True)
    return "".join(map(str, list_1d))


##
# DEBUG
##



DEBUG = True
def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


# example
# drint(f"[debug] 嘗試加入: {word}, 當前行長: {tentative_len}")


##
# str alone
##

def is_int(str1):
    nums = "0123456789"
    for ch in str1:
        if not ch in nums:
            return False
    return True

def is_float(str1):
    nums = "0123456789."
    for ch in str1:
        if not ch in nums:
            return False
    return True


def reverse (num: int) -> int:
    return int(str(num)[::-1])


# @param a str
# @param b int
# ex: 1432219, 3 -> 1219
def remove_digit_min(a, b):
    stack = []
    for digit in a:
        while b > 0 and stack and stack[-1] > digit:
            stack.pop()
            b -= 1
        stack.append(digit)

    # 若還沒刪夠，從後面刪
    while b > 0:
        stack.pop()
        b -= 1

    result = "".join(stack).lstrip("0")
    return result if result else "0"



# @return list[int]
# ex: [1, 2, 3, 3, 4, 5], 3 -> [2, 3]
def find_all_value_idx(list_1d, target):
    return [idx for idx, val in enumerate(list_1d) if val == target]


# @return list[val_t]
# ex: [1, 2, 3, 3, 4, 5], 3 -> [3, 3]
def find_all_value_val(list_1d, target):
    return [val for idx, val in enumerate(list_1d) if val == target]



# @return list_1d[str]
# 把 str1 的長度 len1 的連續子字串組成 list 返回
# ex: 2, "1234" -> ["12", "23", "34"]
def get_substr (len1, str1):
    s = 0
    e = len(str1) - 1
    ret = []
    while s + len1 - 1 <= e:
        ret.append( str1[s:s+len1] )
        s += 1
    return ret




def partition_str_1 (str1, n):
    for i in range( math.ceil(len(str1) / n ) ):
        ans.append( str1[i * n:i * n + n] )
    return ans

# ex:
# ("123456", 2) -> ["12", "34", "56"]
# ("1234567", 4) -> ["1234", "567"]

def make_line(words: list[str], length: int) -> str:
    """格式化成符合長度的行（最後一個單字後補空格）"""
    if not words:
        return ""

    space_len = len(words) -1
    total_len = sum(len(w) for w in words) + space_len
    space_count = length - total_len

    if len(words) == 1:
        return words[0] + ' ' * space_count

    return ' '.join(words[:-1]) + ' ' * (space_count + 1) + words[-1]

# 把 list 變為 str, 以 ' ' 連接，保證長度等於 length
# 長度不足則在 str[-1]. str[-2] 間補 " "
# ex: ["Hi", "O", "You"], 10 -> "Hi O   You"


##
# Matrix (list_2d)
##



def flip_2d(list_2d):
    new_list_2d = []
    for list_1d in list_2d[::-1]:
        new_list_2d.append(list_1d)
    return new_list_2d

def transpose_2d(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]

def rotate_left_2d(list_2d):
    return flip_2d( transpose_2d(list_2d) )

def rotate_right_2d (list_2d):
    return transpose_2d(flip_2d(list_2d))

# ex: (1, 3) -> [[1,2,3],[4,5,6],[7,8,9]]
def gen_square_2d(s, len1):
    list_2d = []
    for i in range(len1):
        list_1d = []
        for j in range(s, s + len1):
            list_1d.append(i*len1 + j)
        list_2d.append(list_1d)
    return list_2d




##
# 2D
##

def dist(x1, y1, x2, y2 ) -> float:
    """兩點距離"""
    return math.sqrt( pow( x1 - x2, 2) + pow(y1 - y2, 2)  )

def is_inside_circle(c_x, c_y, c_len, x, y):
    if dist (c_x, c_y, x, y) <= c_len:
        return True
    else:
        return False


# lens 有三數字，代表三角形的邊長
def is_triangle(lens):
    lens.sort()
    if lens[0] + lens[1] > lens[2]:
        return True
    else:
        return False

##
# Base
##

def to_base(n: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

##
# Math
##

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

def factorial (num: int) -> int:
    if num == 0:
        return 1
    ret = 1
    for i in range(2,num+1):
        ret *= i
    return ret

##
# DP
##

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

# 分兩堆，求最小差距
# ex:
# [5, 13, 21, 30, 35] -> 2
# 5+13+35 - 21+30 = 53 - 51 = 2



def number_combinations(n, coin_1d):
    dp_3d = [[] for _ in range(n + 1)]
    dp_3d[0] = [[]]  # 組成 0 元的方式是一個空組合

    for coin in coin_1d:
        for pos_val in range(coin, n+1):
            for dp_1d in dp_3d[pos_val - coin]:
                dp_3d[pos_val].append(dp_1d + [coin] )
    return dp_3d[n]
# 對一個數字，求其由其他數字組成的所有方法
# ex:
# 10, [1, 5, 10] -> [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 5], [5, 5], [10]]

##
# interval
##

from collections import defaultdict

def interval_interval(intervals):
    intervals.sort(key=lambda x: x[0])  # sort by start time

    heap = []  # (interval end, id)

    dict1 = defaultdict(list) # [id, interval]
    car_id_counter = 1  # 車號 1

    for interval in intervals:
        start, end = interval

        if heap and heap[0][0] <= start: # heap[0] 是 tuple，使用 [0] 存取 tuple
            # 有車可以用（最早空的車）
            old_end, car_id = heapq.heappop(heap)
        else:
            # 沒車用，派新車
            car_id = car_id_counter
            car_id_counter += 1

        dict1[car_id].append(interval)
        heapq.heappush(heap, (end, car_id))

    return dict1

# 公車發車，最少公車數
# ex: [[1, 5], [7, 12], [9, 18]] -> 2
def interval_min_value(interval_1d):
    interval_1d.sort()
    heap = []
    for interval in interval_1d:
        s, e = interval
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)


# 重疊區間合併，總區間長度
# ex: [[0, 6], [4, 10]] -> 10
def interval_combine_min_bad(interval_1d):
    interval_1d.sort()
    sum1 = 0
    heap = []
    for interval in interval_1d:
        if heap and heap[0][1] > interval[0] and heap[0][1] >= interval[1]:
            # 包含情況，不做事
            pass
        elif heap and heap[0][1] > interval[0] and heap[0][1] < interval[1]:
            # 重疊發生
            # 第三段用於避免包含的情況
            tmp = heap[0][0]
            heapq.heappop(heap)
            heapq.heappush(heap, (tmp, interval[1]))
        elif heap:
            # 重疊沒發生
            sum1 += heap[0][1] - heap[0][0]
            heapq.heappop(heap)
            heapq.heappush(heap, (interval[0], interval[1]))
        else:
            # 目前沒有
            heapq.heappush(heap, (interval[0], interval[1]))

    sum1 += heap[0][1] - heap[0][0]
    return sum1

# 重疊區間合併，總區間長度
# ex: [[0, 6], [4, 10]] -> 10
def interval_combine_min(interval_1d):
    interval_1d.sort()
    merged = []
    for start, end in interval_1d:
        if not merged or merged[-1][1] < start:
            # 沒有重疊
            merged.append((start, end))
        else:
            # 重疊
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    # 計算總長度
    sum1 = sum(e - s for s, e in merged)
    return sum1





