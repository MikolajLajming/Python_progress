import turtle
import random


def ordinal(i):
    k = i % 10
    return str("%d%s" % (i, "tsnrhtdd"[(i / 10 % 10 != 1) * (k < 4) * k::4]))


screen = turtle.Screen()
screen.setup(width=800, height=600)
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
user_bet = ""
can_we_go_on = False
while not can_we_go_on:
    user_bet = screen.textinput(title="What is your bet?", prompt=f"Type in one of the colors: {', '.join(colors)}")
    if user_bet.lower() not in colors:
        user_bet = screen.textinput(title="What is your bet?", prompt=f"Type in one of the colors: {', '.join(colors)}")
    else:
        can_we_go_on = True
print(f"You've bet on {user_bet.title()}")
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
    color = i
    contestant = turtle.Turtle(shape="turtle")
    contestant.color(color)
    contestant.penup()
    contestant.goto(-380, turtle_starting_height)
    contestant.speed("slow")
    turtle_starting_height += 40
    turtles[color] = contestant

turtles[user_bet].pencolor("black")

end_race = False
winner = ""
turtles_finished = []
x = 1
bet_position = 0
while not end_race:
    turtle_positions = []
    for i in turtles:
        turtles[i].forward(random.randint(0, 10))
        turtle_positions.append(turtles[i].pos()[0])
        if turtles[i].pos()[0] > 345 and winner == "":
            winner = i
            turtles_finished.append(i)
            print(f"{x} position: {i.title()}")
            x += 1
        if turtles[i].pos()[0] > 345 and winner != "" and i not in turtles_finished:
            turtles_finished.append(i)
            print(f"{x} position: {i.title()}")
            if i == user_bet:
                bet_position = x
                x += 1
            else:
                x += 1
    if min(turtle_positions) > 385:
        end_race = True

print(f"{winner.title()} won!")
if user_bet == winner:
    print(f"Congrats!")
else:
    print(f"Your turtle finished {ordinal(bet_position)}. You lost!")

screen.exitonclick()