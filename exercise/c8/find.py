def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def find_with_index(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


