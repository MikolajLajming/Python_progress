from turtle import Turtle
from random import uniform, getrandbits
import numpy as np
from math import fabs

BALL_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.last_x_position = 0
        self.last_y_position = 0
        self.angle = 0
        self.going_up = 0
        self.towards_right = 0

    def save_position(self):
        self.last_x_position = self.xcor()
        self.last_y_position = self.ycor()

    def move(self, towards_right, going_up):
        self.save_position()
        y_speed = fabs(np.sin(self.angle * (np.pi/180))) if going_up \
            else (fabs(np.sin(self.angle * (np.pi/180))) * -1)
        x_speed = fabs(np.cos(self.angle * (np.pi/180))) if towards_right \
            else (fabs(np.cos(self.angle * (np.pi/180))) * -1)
        self.goto((self.last_x_position + (x_speed * BALL_SPEED)), (self.last_y_position + (y_speed * BALL_SPEED)))

    def move_ball(self, paddle_hit, top_half):
        self.going_up = True if self.last_y_position < self.ycor() else False
        if self.ycor() >= 285 and self.going_up or self.ycor() <= - 285 and not self.going_up:
            self.going_up = not self.going_up
        self.towards_right = True if self.last_x_position < self.xcor() else False
        if paddle_hit:
            self.towards_right = not self.towards_right
            self.going_up = top_half
        self.move(towards_right=self.towards_right, going_up=self.going_up)

    def initial_move(self, towards_right):
        self.goto(0, uniform(-285, 285))
        coin_flip = getrandbits(1)
        self.angle = 45
        if coin_flip:
            self.move(towards_right=towards_right, going_up=coin_flip)
        else:
            self.move(towards_right=towards_right, going_up=coin_flip)

    def serve_ball(self, towards_right):
        self.last_x_position = 0
        self.last_y_position = 0
        self.initial_move(towards_right)

    def hide_ball(self):
        self.hideturtle()

    def show_ball(self):
        self.showturtle()
