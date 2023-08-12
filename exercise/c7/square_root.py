import math


def square_root(a):
    x = a / 2 + 1
    """
    接收一个形参a，选择一个合理的值x，并返回a的平方根的估计值
    :param a:
    :param x:
    :return:
    """
    epsilon = 0.0000001
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


def test_square_root(a):
    print(a, end=" ")
    x = square_root(a)
    print(x, end=" ")
    y = math.sqrt(a)
    print(y, end=" ")
    print(abs(x - y))


z = 9
while z > 0:
    test_square_root(z)
    z = z - 1
