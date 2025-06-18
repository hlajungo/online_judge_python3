# str1 = input()

# i = 0
# while i < len(str1):
    # cur_num = str1[i]
    # j = 0
    # while j < int(cur_num):
        # print("*", end="")
        # j+=1
    # print()
    # i+=1

# provided by chatGPT
# start chatGPT
str1 = input()

for ch in str1:
    print("*" * int(ch))
# end chatGPT

