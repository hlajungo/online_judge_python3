# dict is hash map
# belove python 3.7, is unordered map
# otherwise is map, order is deterministic
dict1 = {
    "dog": "狗",
    "狗" : "dog",
    "cat": "貓",
    "貓": "cat",
    "duck": "鴨",
    "鴨": "duck",
    "cow": "牛",
    "牛": "cow",
    "fox": "狐",
    "狐": "fox"
}

str1 = input()

print(dict1[str1])
