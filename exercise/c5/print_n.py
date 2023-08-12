"""
 将字符串 s 打印 n 次
"""


def print_n(s, n):
    """
    使用递归（recursive）实现
    :param s:  被打印的字符串s
    :param n: 字符串s被打印的次数
    :return:
    """
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)


def print_n(s, n):
    """
    使用循环（loop）实现
    :param s:
    :param n:
    :return:
    """
    while n > 0:
        print(s)
        n = n - 1


print_n('1', 10)
