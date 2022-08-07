import colorgram
import turtle as t
import random

number_of_colors = 34
color_package = colorgram.extract('image.jpg', number_of_colors)
colors = [(color_package[x].rgb.r, color_package[x].rgb.g, color_package[x].rgb.b) for x in range(number_of_colors)]

# first 4 colors in this image are shades of light grey - getting rid of them
for i in range(4):
    del colors[0]

mortimer = t.Turtle()
mortimer.speed(5)
t.colormode(255)

def draw_row(length):
    for x in range(length):
        mortimer.dot(20, random.choice(colors))
        mortimer.forward(50)

def new_row(way_back):
    mortimer.setheading(90)
    mortimer.forward(50)
    mortimer.setheading(180)
    mortimer.forward(way_back * 50)
    mortimer.setheading(0)


def draw_hirst(height, width):
    mortimer.penup()
    mortimer.setposition(-250, -250)
    for _ in range(height):
        draw_row(width)
        new_row(width)
    mortimer.setposition(-250, -250)
    mortimer.hideturtle()


draw_hirst(10, 10)

my_screen = t.Screen()
my_screen.exitonclick()




