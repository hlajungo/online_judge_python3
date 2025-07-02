import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

# list_1d = list(map(int, input().split()) )
n = int(input())
list_1d = []
for i in range(n):
    a, b = map(int, input().split())
    list_1d.append((a,b))

list_1d.sort()
sum1 = 0
heap = []
# 0 4, 1 2
for interval in list_1d:
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


print(sum1)









