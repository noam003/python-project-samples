from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_score(self, won_game):
        if won_game:
            self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", align="left", font=("Courier", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=("Courier", 20, "normal"))

    def reset(self):
        self.clear()