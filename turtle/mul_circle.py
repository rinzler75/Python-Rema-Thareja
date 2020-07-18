import turtle as t
t.bgcolor("yellow")
t.color("red")
t.pensize(10)
for angle in range(0,360,30):
    t.seth(angle)
    t.circle(100)
t.exitonclick()