import math
import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# polygon 多边形
def polygon(t, n, length):
    """
    多边形
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)


#  polyline 多边线
def polyline(t, n, length, angle):
    """
    使 t 画一个给定 length 以及 angle（度）的 n 条线段
    进一步对 polygon 函数泛化
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    arc(t, r, 360)


def arc(t, r, angle):
    # 根据 圆的周长公式 2 * pi * r，计算半径r的圆周长
    arc_length = 2 * math.pi * r * abs(angle) / 360
    # 利用周长计算合适的圆的边长（为什么是这个公式，可以画出合适的圆？）
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()