def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    """
    get middle string of word
    :param word:
    :return: middle string of word ,if word has one/two/empty char ,then return empty
    """
    return word[1:-1]


# middle func unit case
# print(middle("skd"))
# print(middle("sskd"))
# print(middle(""))
# print(middle("sk"))
# print(middle("s"))


def is_palindrome(word):
    if first(word) == last(word):
        middles = middle(word)
        if len(middles) == 0:
            return True
        return is_palindrome(middles)
    return False


print(is_palindrome("bbssbbb"))
print(is_palindrome("allen"))
print(is_palindrome("otto"))
print(is_palindrome("redivider"))
