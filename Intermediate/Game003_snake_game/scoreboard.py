from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("RED")
    #     self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
