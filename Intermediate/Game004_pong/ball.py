from turtle import Turtle
from random import randint, uniform

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

    def save_position(self):
        self.last_x_position = self.xcor()
        self.last_y_position = self.ycor()


    def move(self, towards_right, going_up):
        self.save_position()
        x_speed = BALL_SPEED if towards_right else (BALL_SPEED * -1)
        y_speed = (self.angle * BALL_SPEED) if going_up else (self.angle * -1 * BALL_SPEED)
        self.goto((self.last_x_position + x_speed), (self.last_y_position + y_speed))

    def move_ball(self, hit_paddle):
        towards_right = True if self.last_x_position < self.xcor() else False
        if hit_paddle:
            towards_right = not towards_right
        going_up = True if self.last_y_position < self.ycor() else False
        if self.ycor() >= 280 or self.ycor() <= - 280:
            going_up = not going_up
        self.move(towards_right=towards_right, going_up=going_up)

    def initial_move(self):
        self.goto(0, uniform(-280, 280))
        coin_flip = randint(0, 1)
        self.angle = uniform(0, 1)
        if coin_flip == 0:
            self.move(towards_right=True, going_up=True)
        else:
            self.move(towards_right=True, going_up=False)

    def reset(self):
        self.goto(0, 0)
