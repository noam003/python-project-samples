from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:

    def create_snake(self):
        for position in STARTING_POSITIONS:
            s = Turtle("square")
            s.color("white")
            s.penup()
            s.setpos(position)
            self.segments.append(s)

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setpos(new_x, new_y)
        self.head.forward(DISTANCE)

    def add_seg(self):
        s = Turtle("square")
        s.color("white")
        s.penup()
        x_last = self.segments[len(self.segments) - 1].xcor()
        y_last = self.segments[len(self.segments) - 1].ycor()
        s.setpos(x_last, y_last)
        self.segments.append(s)

    def reset(self):
        for each_seg in self.segments:
            each_seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


