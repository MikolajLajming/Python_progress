from turtle import Turtle


class Stripes(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-400, -300)
        self.pendown()
        self.goto(400, -300)
        self.goto(400, 300)
        self.goto(-400, 300)
        self.goto(-400, -300)
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.pendown()
        self.forward(5)
        self.penup()
        self.forward(10)
        for i in range(29):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.pendown()
        self.forward(5)