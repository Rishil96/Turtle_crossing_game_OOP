from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.update_level()

    def update_level(self):
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Final Score: {self.score - 1}", align="center", font=FONT)
