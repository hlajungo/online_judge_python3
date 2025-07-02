import math
import sys
import heapq

DEBUG = True

def drint(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)

n = int(input())
interval_1d = []
for i in range(n):
    a, b = map(int, input().split())
    interval_1d.append([a, b])


# 這個問題表象出來的邏輯骨架，居然可以捨棄這麼多的資訊，如此排序可以造成邏輯的形成，只需要一個關鍵情況就能解決
# 驚訝的是，他有一個前置的 if，這在一開始不會觸發，他是為之後設計的
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

def interval_min_value(interval_1d):
    interval_1d.sort()
    heap = []
    for interval in interval_1d:
        s, e = interval
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)

# ex:
# [[1, 5], [7, 12], [9, 18]] -> 2

# print(interval_interval(interval_2d))
print(interval_min_value(interval_1d) )




