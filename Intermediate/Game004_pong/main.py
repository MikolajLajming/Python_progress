from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.update()
ball.initial_move(True)
screen.update()

game_on = True
while game_on:
    screen.update()
    ball_x_cor = ball.xcor()
    ball_y_cor = ball.ycor()
    r_paddle_y_cor = r_paddle.ycor()
    l_paddle_y_cor = l_paddle.ycor()
    n = 1
    if ball_x_cor >= 325 or ball_x_cor <= -325:
        right_paddle = True if ball_x_cor >= 325 else False
        if ( r_paddle_y_cor - 60) < ball_y_cor < (r_paddle_y_cor + 60) or (l_paddle_y_cor - 60) < ball_y_cor < (l_paddle_y_cor + 60):
            paddle_y_cor = r_paddle_y_cor if ball_x_cor > 0 else l_paddle_y_cor
            if ball_y_cor > paddle_y_cor:
                ball.angle = (dist([paddle_y_cor], [ball.ycor()]) / 60) * 2
                ball.move_ball(True, True)
            elif ball_y_cor <= paddle_y_cor:
                ball.angle = (dist([paddle_y_cor], [ball.ycor()]) / 60) * 2
                ball.move_ball(True, False)
        else:
            if right_paddle:
                scoreboard.P2_score += 1
                ball.reset_ball(right_paddle)
            else:
                scoreboard.P1_score += 1
                ball.reset_ball(right_paddle)
    else:
        ball.move_ball(False, False)
    time.sleep(0.05)



screen.exitonclick()