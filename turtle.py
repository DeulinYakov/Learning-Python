import turtle

window = turtle.Screen()
window.bgcolor('gold')
window.setup (500, 400)
window.title("Черепашка")

turtle = turtle.Turtle('green')
turtle.color('black')
turtle.shapesize(0.5)
turtle.showturtle()


window.exitonclick()
window.mainloop()