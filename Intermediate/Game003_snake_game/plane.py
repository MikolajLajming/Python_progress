from turtle import Turtle

class Plane(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-275, -275)
        self.pendown()
        self.goto(-275, 275)
        self.goto(275, 275)
        self.goto(275, -275)
        self.goto(-275, -275)
        self.penup()