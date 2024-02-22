from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from math import dist
from board import Stripes
import random
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


def update_screen():
    screen.update()
    time.sleep(0.02)


def finish_turn(who_lost):
    for i in range(10):
        ball.move_ball(False, False)
        update_screen()
    scoreboard.increase_score(not who_lost)
    for i in range(50):
        update_screen()
    ball.serve_ball(who_lost)


update_screen()
ball.initial_move(bool(random.getrandbits(1)))
update_screen()
time.sleep(1)
game_on = True

while game_on:
    if scoreboard.P2_score >= 10 or scoreboard.P1_score >= 10:
        game_on = False
        scoreboard.game_over()
        ball.hide_ball()
        screen.update()
    else:
        screen.update()
        ball_x_cor = ball.xcor()
        ball_y_cor = ball.ycor()
        r_paddle_y_cor = r_paddle.ycor()
        l_paddle_y_cor = l_paddle.ycor()
        if ball_x_cor >= 350 or ball_x_cor <= -350:
            ball_x_cor = ball.last_x_position
            ball_y_cor = ball.last_y_position
            right_side = True if ball_x_cor > 0 else False
            if (r_paddle_y_cor - 65) < ball_y_cor < (r_paddle_y_cor + 65) and right_side \
                    or (l_paddle_y_cor - 65) < ball_y_cor < (l_paddle_y_cor + 65) and not right_side:
                paddle_y_cor = r_paddle_y_cor if right_side else l_paddle_y_cor
                if ball_y_cor > paddle_y_cor:
                    ball.angle = (((dist([paddle_y_cor], [ball.ycor()])) / 65) * 90) + 1
                    print(ball.angle)
                    ball.move_ball(True, True)
                    update_screen()
                elif ball_y_cor <= paddle_y_cor:
                    ball.angle = (((dist([paddle_y_cor], [ball.ycor()])) / 65) * 90) + 1
                    print(ball.angle)
                    ball.move_ball(True, False)
                    update_screen()
            else:
                did_right_player_lost = right_side
                if did_right_player_lost:
                    finish_turn(who_lost=did_right_player_lost)
                else:
                    finish_turn(who_lost=did_right_player_lost)
        else:
            ball.move_ball(False, False)
            update_screen()

screen.exitonclick()