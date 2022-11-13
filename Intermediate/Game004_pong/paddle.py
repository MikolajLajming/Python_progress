from turtle import Turtle

MOVE_DISTANCE = 20
HEADING_UP = 90
HEADING_DOWN = 270


class Paddle(Turtle):

    def __init__(self, player=bool):
        super().__init__()
        self.player = player
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(350, 0) if player else self.goto(-350, 0)

    def go_up(self):
        if self.ycor() <= 220:
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() >= -220:
            self.backward(MOVE_DISTANCE)
