import turtle
hi=turtle.Turtle()
hi.shape("turtle")
hi.penup()
for i in range(0,100,5):
    hi.forward(30+i)
    hi.left(30)
    hi.stamp()