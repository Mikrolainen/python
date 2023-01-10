import turtle


aken = turtle.Screen()
aken.setup(300,300)
aken.title("kilpkonna harjutus 02")


konn1 = turtle.Turtle()
for x in range(5):
    konn1.forward(100)
    konn1.right(144)

konn2 = turtle.Turtle()
konn2.color("red")
konn2.left(135)
konn2.forward(100)
konn2.left(90)
konn2.forward(100)
konn2.left(135)
konn2.forward(140)

turtle.exitonclick()

