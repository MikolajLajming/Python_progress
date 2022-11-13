from turtle import Screen
from paddle import Paddle
from ball import Ball
from math import dist
import time

screen = Screen()
screen.setup(800, 600, 0, 0)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(True)
l_paddle = Paddle(False)
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.update()
ball.initial_move()
screen.update()

game_on = True
while game_on:
    screen.update()
    ball_x_cor = ball.xcor()
    ball_y_cor = ball.ycor()
    r_paddle_y_cor = r_paddle.ycor()
    l_paddle_y_cor = l_paddle.ycor()
    if ball_x_cor >= 330 and (ball_y_cor - 50) < r_paddle_y_cor < (ball_y_cor + 50)\
            or ball_x_cor <= -330 and (ball_y_cor - 50) < l_paddle_y_cor < (ball_y_cor + 50):
        paddle_y_cor = r_paddle_y_cor if ball_x_cor > 0 else l_paddle_y_cor
        ball.angle = (dist([paddle_y_cor], [ball.ycor()])/50)
        ball.move_ball(True)
    else:
        ball.move_ball(False)
    time.sleep(0.05)



screen.exitonclick()