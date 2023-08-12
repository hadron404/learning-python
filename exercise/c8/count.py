from find import find_with_index


def cnt_word(word, s):
    count = 0
    index = -1
    while index < len(word):
        b = find_with_index(word, s, index+1)
        if b == -1:
            return count
        count += 1
        index = b
    return count


print(cnt_word("asdfdsababa", 'a'))
print(find_with_index("ababa", 'a',2))

