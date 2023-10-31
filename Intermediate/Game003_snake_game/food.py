from turtle import Turtle
from random import randint
from snake import SEGMENT_POSITIONS


def divisible_random(a=-260, b=260, n=20):
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
        self.refresh(SEGMENT_POSITIONS)

    def refresh(self, snake_position):
        new_position = (divisible_random(), divisible_random())
        if new_position not in snake_position:
            self.goto(new_position)
