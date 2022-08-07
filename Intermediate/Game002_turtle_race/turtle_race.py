import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
user_bet = screen.textinput(title="What is your bet?", prompt=f"Type in one of the colors: {', '.join(colors)}")
print(f"Your bet is {user_bet.title()}")
turtles = {}
judge = turtle.Turtle(shape="turtle")
judge.speed("fast")
for i in [-1, 1]:
    judge.penup()
    judge.towards(365*i, -180)
    judge.goto(365*i, -180)
    judge.pendown()
    judge.setheading(90)
    judge.forward(320)
judge.setheading(270)

turtle_starting_height = -120
for i in colors:
    contestant = turtle.Turtle(shape="turtle")
    contestant.color(i)
    contestant.penup()
    contestant.goto(-380, turtle_starting_height)
    turtle_starting_height += 40
    turtles[i] = contestant

print(turtles)

win = False
winner = ""
turtles_finished = []
x = 1
while not win:
    turtle_positions = []
    for i in turtles:
        turtles[i].forward(random.randint(0, 10))
        turtle_positions.append(turtles[i].pos()[0])
        if turtles[i].pos()[0] > 350 and winner == "":
            winner = i
            turtles_finished.append(i)
            print(f"{x} position: {i.title()}")
            x += 1
        if turtles[i].pos()[0] > 350 and winner != "" and i not in turtles_finished:
            turtles_finished.append(i)
            print(f"{x} position: {i.title()}")
            x += 1
    if min(turtle_positions) > 380:
        win = True

print(f"{winner.title()} won!")
if user_bet == winner:
    print(f"Congrats!")
else:
    print(f"You lost!")

screen.exitonclick()