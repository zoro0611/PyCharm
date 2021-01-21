import turtle
jerry = turtle.Turtle()
jerry.speed(100)
jerry.shape("turtle")
jerry.color("green")

for x in range(1,100): # x = 1~99
    jerry.circle(100)
    jerry.left(360/x)

turtle.done()