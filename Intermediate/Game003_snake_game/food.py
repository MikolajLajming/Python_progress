from turtle import Turtle
from random import randint


def divisible_random(a=-280, b=280, n=20):
    result = randint(a, b)
    while result % n != 0:
        result = randint(a, b)
    return result


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(divisible_random(), divisible_random())