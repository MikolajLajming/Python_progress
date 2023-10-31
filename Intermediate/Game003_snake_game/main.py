from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from plane import Plane

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python's Snake xD")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
plane = Plane()
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_on = True
while game_on:
    screen.update()
    snake_position = []
    for n in snake.segments:
        snake_position.append(n.pos())
        if n != snake.head and snake.head.distance(n.pos()) < 1:
            game_on = False
    if snake.head.xcor() >= 270 or snake.head.ycor() >= 270 or snake.head.xcor() <= -270 or snake.head.ycor() <= -270:
        game_on = False
    if snake.head.distance(food) < 10:
        food.refresh(snake_position)
        snake.extend_snake()
        scoreboard.increase_score()
        screen.update()
    if not game_on:
        scoreboard.reset()
        snake.snake_reset()
        screen.update()
        game_on = True
    else:
        snake.move()
    time.sleep(0.2)




screen.exitonclick()