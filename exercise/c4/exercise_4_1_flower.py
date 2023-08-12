import turtle

from polygon import arc


def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        bob.lt(360 / n)


bob = turtle.Turtle()

flower(bob, 100, 30, 60)

turtle.mainloop()
