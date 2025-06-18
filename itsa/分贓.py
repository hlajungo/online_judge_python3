import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):


# >> TC: O(n * total/2)
# >> SC: O(total/2)
def partition_2_min_diff(nums: list) -> int:
    total = sum(nums)
    n = len(nums)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

# 有一個 pool "dp"，一開始只有 0, 通過不斷接觸新的 num 來擴充 dp
# 例如有 10，0+10=10，可到達 0 10
# 然後有 20, 0+20=20, 10+20=30, 現在 0 10 20 30 可到達
# 上述操作要變成代碼
# 我們需要接觸新的物件，把原有池中成員和物件變成新的可到達區域

# 遍歷 所有物件
#   從 中間 到 num (反著來是為了處理依賴性，結束是 num 是因為 j-num 會溢位)
#       當前物件 = 當前物件 或 能通過得到 num 到達

    for num in nums:
        for j in range(target, num - 1, -1): 
            dp[j] = dp[j] or dp[j - num]

    for i in range(target, -1, -1):
        if dp[i]:
            return total - 2 * i  # 差值 = |(total - i) - i| = total - 2i
# "兩堆最小差值" 的最優情況是兩堆相等，其餘情況是有差值，可以想成一個數列，相等於 "所有能到達的數字中，最靠近中間的那個數字" 
# "bool_arrayize" 從原本數字 N，變成儲存每個數字能否到達 bool_array


n = input()
list1 = list(map(int, input().split()) )
dif = partition_2_min_diff(list1)
print (dif)
