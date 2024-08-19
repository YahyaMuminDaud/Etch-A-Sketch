from turtle import Turtle, Screen
from movement import Movement

screen = Screen()
screen.title("Etch-A-Sketch")
movement = Movement()


screen.listen()
screen.onkey(movement.move_up, "Up")
screen.onkey(movement.move_down, "Down")
screen.onkey(movement.move_left, "Left")
screen.onkey(movement.move_right, "Right")
screen.onkey(movement.clearing, "c")







screen.exitonclick()