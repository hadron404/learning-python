import math


def factorial(n):
    """
    求n的阶乘
    :param n:
    :return:
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def pi():
    factor = 2 * math.sqrt(2) / 9801
    total = 0
    k = 0
    while True:
        x = factorial(4 * k) * (1103 + 26390 * k)
        y = factorial(k) ** 4 * 396 ** (4 * k)
        result = x / y
        term = factor * result
        if abs(term) < 1e-15:
            break
        k = k + 1
        total = total + result

    return 1 / (factor * total)
