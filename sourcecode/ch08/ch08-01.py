import turtle

length = 20
angle = 90

p = turtle.Pen()

for i in range(0, 10):
    p.forward(length)
    p.right(angle)
    p.forward(length)
    p.left(angle)


    
