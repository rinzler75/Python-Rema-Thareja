import turtle
color=["red","green","blue","orange"]
for i in range(1,5):
    turtle.color(color[i-1])
    turtle.left(i*10)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.exitonclick()