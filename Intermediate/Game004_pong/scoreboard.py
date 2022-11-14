from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.P1_score = 0
        self.P2_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 255)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 255)
        self.write(f"{self.P2_score} : {self.P1_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self, p1=bool):
        if p1:
            self.P1_score += 1
        else:
            self.P2_score += 1
        self.clear()
        self.update_score()

    # def pause(self):
    #     self.goto(0, 0)
    #     self.write("PAUSE\nPress P to resume, Q to quit", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))
