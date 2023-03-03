from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.shape("turtle")
        self.color("black")

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def won_check(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        self.hideturtle()
        self.__init__()


