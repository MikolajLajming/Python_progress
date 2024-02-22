from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.P1_score = 0
        self.P2_score = 0
        self.color("white")
        self.penup()
        self.goto(-340, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-330, 260)
        self.write(self.P2_score, align="center", font=("Consolas", 24, "bold"))
        self.goto(330, 260)
        self.write(self.P1_score, align="center", font=("Consolas", 24, "bold"))


    def increase_score(self, p1=bool):
        if p1:
            self.P1_score += 1
        else:
            self.P2_score += 1
        self.update_score()

    # def pause(self):
    #     self.goto(0, 0)
    #     self.write("PAUSE\nPress P to resume, Q to quit", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Consolas", 24, "normal"))
