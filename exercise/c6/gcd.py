"""
接收形参a和b，并返回它们的最大公约数
"""


def gcd(a, b):
    """
    更相减损法实现
    :param a:
    :param b:
    :return: a和b的最大公约数
    """
    # print(a, b)
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(b - a, a)


def gcd(a, b):
    """
    欧几里得算法（辗转相除法）实现
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    return gcd(a % b, a)

# print(gcd(1691169, 13113))
