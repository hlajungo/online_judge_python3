DEBUG = False

def drinf(*args, **kwargs):
    """條件式 debug 輸出"""
    if DEBUG:
        print(*args, **kwargs)



# 把 list 變為 str, 以 ' ' 連接，保證長度等於 length
# 長度不足則在 str[-1]. str[-2] 間補 " "
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


def break_line(words: list[str], line_len: int):
    """主處理函數：斷行顯示字串"""
    cur_words = []
    cur_len = 0

    for word in words:
        tentative_len = cur_len + len(word) + (1 if cur_words else 0)

        drinf(f"[debug] 嘗試加入: {word}, 當前行長: {tentative_len}")

        # 加入當前行
        if tentative_len < line_len:
            cur_words.append(word)
            cur_len = tentative_len
        # 加入當前行後輸出
        elif tentative_len == line_len:
            cur_words.append(word)
            print(make_line(cur_words, line_len))
            cur_words.clear()
            cur_len = 0
        else:
            # 字要在新行，但當前只有一個字
            if len(cur_words) == 1:
                temp_line = cur_words[0] + " " + word
                print(temp_line[:line_len - 1] + "-")

                remainder = temp_line[line_len - 1:].strip()
                cur_words = [remainder] if remainder else []
                cur_len = len(remainder) + 1 if remainder else 0
            else:
                print(make_line(cur_words, line_len))
                cur_words = [word]
                cur_len = len(word) + 1

    # 收尾
    if cur_words:
        print(make_line(cur_words, line_len))

if __name__ == "__main__":
    len_line = int(input("輸入一行長度："))
    words = input("輸入字串：").split()
    break_line(words, len_line)

