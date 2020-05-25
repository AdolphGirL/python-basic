import turtle


sides = int(input("請輸入多邊形: "))

angle = 360.0 / sides
length = 400.0 / sides

p = turtle.Pen()
p.fillcolor('blue')
p.begin_fill()

for side in range(sides):
    p.forward(length)
    p.right(angle)

p.end_fill()
    
    
