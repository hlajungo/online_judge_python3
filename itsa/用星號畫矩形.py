nums = list(map(int, input().split()))
# map (type, list) -> <map object>
# 把 list 中每個元素進行 type 轉換
# map 是 built-in function
#built-in function 有這些 https://docs.python.org/3/library/functions.html

# list(<map object>) -> list

# str.split() -> list


# for i in range(nums[1]):
    # print("*" * int(nums[0]))

print( ("*" * nums[0] + '\n' ) * nums[1], end="")

