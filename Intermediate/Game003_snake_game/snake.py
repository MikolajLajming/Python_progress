from turtle import Turtle

SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
CEMENTARY = (1000, 1000)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.neck = self.segments[1]
        self.head = self.segments[0]

    def create_snake(self):
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.ycor() + MOVE_DISTANCE != self.neck.ycor():
            self.head.setheading(UP)

    def down(self):
        if self.head.ycor() - MOVE_DISTANCE != self.neck.ycor():
            self.head.setheading(DOWN)

    def right(self):
        if self.head.xcor() + MOVE_DISTANCE != self.neck.xcor():
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.xcor() - MOVE_DISTANCE != self.neck.xcor():
            self.head.setheading(LEFT)

    def snake_reset(self):
        for i in self.segments:
            i.goto(CEMENTARY)
        self.segments.clear()
        self.create_snake()
        self.neck = self.segments[1]
        self.head = self.segments[0]
