from turtle import Screen
from paddle import Paddle
from ball import Ball, BALL_SPEED
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
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
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
    if ball_x_cor >= 330 or ball_x_cor <= -330:
        right_paddle = True if ball_x_cor > 0 else False
        if (r_paddle_y_cor - 60) < ball_y_cor < (r_paddle_y_cor + 60) and right_paddle \
                or (l_paddle_y_cor - 60) < ball_y_cor < (l_paddle_y_cor + 60) and not right_paddle:
            paddle_y_cor = r_paddle_y_cor if right_paddle else l_paddle_y_cor
            if ball_y_cor > paddle_y_cor:
                ball.angle = (dist([paddle_y_cor], [ball.ycor()])) / 60
                print(ball.angle)
                ball.move_ball(True, True)
            elif ball_y_cor <= paddle_y_cor:
                ball.angle = (dist([paddle_y_cor], [ball.ycor()])) / 60
                print(ball.angle)
                ball.move_ball(True, False)
        else:
            if right_paddle:
                scoreboard.P2_score += 1
                ball.reset_ball(not right_paddle)
                screen.update()
                time.sleep(1)
            else:
                scoreboard.P1_score += 1
                ball.reset_ball(not right_paddle)
                screen.update()
                time.sleep(1)
    else:
        ball.move_ball(False, False)
    time.sleep(0.01)

screen.exitonclick()