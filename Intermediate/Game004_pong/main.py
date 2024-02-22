from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from math import dist
from board import Stripes
import time

screen = Screen()
screen.setup(840, 640, 0, 0)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
stripes = Stripes()
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

game = True
game_on = True

while game:
    time.sleep(1)
    while game_on:
        if scoreboard.P2_score >= 10 or scoreboard.P1_score >= 10:
            game = False
            game_on = False
            scoreboard.game_over()
            ball.hide_ball()
            screen.update()
        else:
            screen.update()
            ball.show_ball()
            ball_x_cor = ball.xcor()
            ball_y_cor = ball.ycor()
            r_paddle_y_cor = r_paddle.ycor()
            l_paddle_y_cor = l_paddle.ycor()
            if ball_x_cor >= 350 or ball_x_cor <= -350:
                right_paddle = True if ball_x_cor > 0 else False
                if (r_paddle_y_cor - 60) < ball_y_cor < (r_paddle_y_cor + 60) and right_paddle \
                        or (l_paddle_y_cor - 60) < ball_y_cor < (l_paddle_y_cor + 60) and not right_paddle:
                    paddle_y_cor = r_paddle_y_cor if right_paddle else l_paddle_y_cor
                    if ball_y_cor > paddle_y_cor:
                        ball.angle = (dist([paddle_y_cor], [ball.ycor()])) / 60
                        ball.move_ball(True, True)
                        screen.update()
                        time.sleep(0.01)
                    elif ball_y_cor <= paddle_y_cor:
                        ball.angle = (dist([paddle_y_cor], [ball.ycor()])) / 60
                        ball.move_ball(True, False)
                        screen.update()
                        time.sleep(0.01)
                else:
                    if right_paddle:
                        for i in range(10):
                            ball.move_ball(False, False)
                            screen.update()
                            time.sleep(0.01)
                        scoreboard.increase_score(False)
                        for i in range(50):
                            screen.update()
                            time.sleep(0.01)
                        ball.reset_ball(not right_paddle)
                    else:
                        for i in range(10):
                            ball.move_ball(False, False)
                            screen.update()
                            time.sleep(0.01)
                        scoreboard.increase_score(True)
                        for i in range(50):
                            screen.update()
                            time.sleep(0.01)
                        ball.reset_ball(not right_paddle)
            else:
                ball.move_ball(False, False)
                screen.update()
                time.sleep(0.01)

screen.exitonclick()