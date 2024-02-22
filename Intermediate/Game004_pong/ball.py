from turtle import Turtle
from random import randint, uniform

BALL_SPEED = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.last_x_position = 0
        self.last_y_position = 0
        self.angle = 1
        self.going_up = 0
        self.towards_right = 0

    def save_position(self):
        self.last_x_position = self.xcor()
        self.last_y_position = self.ycor()

    def move(self, towards_right, going_up):
        self.save_position()
        y_speed = (self.angle * BALL_SPEED) if going_up else (self.angle * BALL_SPEED * -1)
        x_speed = BALL_SPEED if towards_right else (BALL_SPEED * -1)
        self.goto((self.last_x_position + x_speed), (self.last_y_position + y_speed))

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
        coin_flip = randint(0, 1)
        self.angle = uniform(0, 1)
        if coin_flip == 0:
            self.move(towards_right=towards_right, going_up=True)
        else:
            self.move(towards_right=towards_right, going_up=False)

    def reset_ball(self, towards_right):
        self.last_x_position = 0
        self.last_y_position = 0
        self.initial_move(towards_right)

    def hide_ball(self):
        self.hideturtle()

    def show_ball(self):
        self.showturtle()
