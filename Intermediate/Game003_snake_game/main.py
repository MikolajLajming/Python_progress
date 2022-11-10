from snake import Snake
from turtle import Screen
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python's Snake xD")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        print("om nom nom")
        food.refresh()



screen.exitonclick()