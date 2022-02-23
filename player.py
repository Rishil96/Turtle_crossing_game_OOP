from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape('turtle')
        self.color(color)
        self.penup()
        self.goto(-280, 250)
        self.pendown()
        self.width(4)
        self.goto(280, 250)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

