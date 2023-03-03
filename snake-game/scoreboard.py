from turtle import Turtle

STYLE = ('Courier', 20, 'normal')
# write and clear

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        # self.style = ('Courier', 20, 'normal')
        self.score_curr = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score_curr}", font=STYLE, align='center')

    def update(self):
        self.clear()
        self.write(f"Score: {self.score_curr} High score: {self.high_score}", font=STYLE, align='center')

    """def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", font=STYLE, align='center')"""

    def increase_score(self):
        self.score_curr += 1
        self.update()

    def reset(self):
        if self.score_curr > self.high_score:
            with open("data.txt", "r+") as file:
                file.write(str(self.score_curr))
                file.seek(0)
                self.high_score = int(file.read())
        self.score_curr = 0
        self.update()
