from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0,y=220)
        self.write(f"Score = {self.score}", align="center",font=("Courier",18,"normal"))
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}",align="center",font=("Courier",18,"normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game over", align="center", font=("Courier", 30, "normal"))

