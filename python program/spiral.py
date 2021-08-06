import turtle
colors= ['orange','yellow','blue','purple','green','red']
t=turtle.pen()
t.speed(10)
turtle.bgcolor("black")
for i in range(200):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)
    
