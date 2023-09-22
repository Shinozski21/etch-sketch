from turtle import Turtle, Screen

shin = Turtle()
screen = Screen()


def move_forwards():
    shin.forward(10)


def move_backwards():
    shin.backward(10)


def turn_left():
    new_heading = shin.heading() + 10
    shin.setheading(new_heading)


def turn_right():
    new_heading = shin.heading() - 10
    shin.setheading(new_heading)


def clear():
    shin.clear()
    shin.penup()
    shin.home()
    shin.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()