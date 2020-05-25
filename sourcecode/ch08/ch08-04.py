import turtle


def drawShape(p, sides, angle, length):
    for side in range(sides):
        p.forward(length)
        p.right(angle)


def movePen(p, x, y):
    p.penup()
    p.goto(x, y)
    p.pendown()

# 假設是三角形
angle = 360.0 / 3
length = 400.0 / 3

p = turtle.Pen()
movePen(p, -100, 100)
drawShape(p, 3, angle, length)
