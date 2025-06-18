import math

# a, b, c = map(int, (input().split()))

# n = int(input())
# for i in range(n):

# col= map(int, input().split(" "))

def get_len_sum(words):
    sum = 0
    for word in words:
        sum += len(word)
    return sum

len_line = int(input())
words = list(input().split(" "))

print(words)

cur_num = 0
cur_line_word = 0
cur_words = []
cur_len = 0

for word in words:
    cur_line_word += 1
    print(word, cur_len)
    cur_len += len(word) + 1

    if cur_len < len_line: # 小於，沒滿
        print ("smaller")
        cur_len += len(word) + 1
        cur_words.append(word)
    elif cur_len == len_line: # 剛好，則這個字在這行
        print("new_line 1")
        cur_words.append(word)
        cur_len = 0
        cur_line_word = 0
        cur_words.clear()
    elif cur_len > len_line: # 超過，到下一行
        print("new_line 2")
        if cur_line_word == 2: # 此行只有兩字，使用 '-'
            continue
        cur_len = 0
        cur_line_word = 0
        cur_words.clear()
        cur_words.append(word)
        cur_len += len(word) + 1
    print()




