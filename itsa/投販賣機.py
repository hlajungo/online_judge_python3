import math
import sys

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)


"""
dp[A][B] A 快錢
A is 
B is
"""
    # for coin in coins:
        # for amount in range(coin, n + 1):
            # for combo in dp[amount - coin]:
                # new_combo = combo + [coin]
                # dp[amount].append(new_combo)
























def list_change_combinations(n, coin_1d):
    dp_3d = [[] for _ in range(n + 1)]
    dp_3d[0] = [[]]  # 組成 0 元的方式是一個空組合

    for coin in coin_1d:
        for pos_val in range(coin, n+1):
            for dp_1d in dp_3d[pos_val - coin]:
                dp_3d[pos_val].append(dp_1d + [coin] )
    return dp_3d[n]

n = int(input())
coin_1d = list(map(int, input().split() ) )
money = int(input())

combo_2d = list_change_combinations(money, coin_1d)


coin_sum_2d = []
for combo_1d in combo_2d:
    coin_sum_1d = [0] * len(coin_1d)
    for i in combo_1d:
        idx = coin_1d.index(i)
        coin_sum_1d[idx] += 1
    coin_sum_2d.append(coin_sum_1d)

coin_sum_2d.sort()

print(combo_2d)
for coin_sum_1d in coin_sum_2d:
    print("(" + ",".join(map(str, coin_sum_1d)) +")")





