from turtle import Turtle


class Movement(Turtle):

    def __init__(self):
        super().__init__()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.back(10)

    def move_right(self):
        self.right(10)

    def move_left(self):
        self.left(10)

