from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("gold")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 160)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def countdown(self):
        self.goto(0, 0)
        self.write("5", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()
        self.update_scoreboard()

        self.goto(0, 0)
        self.write("4", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()
        self.update_scoreboard()

        self.goto(0, 0)
        self.write("3", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()
        self.update_scoreboard()

        self.goto(0, 0)
        self.write("2", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()
        self.update_scoreboard()

        self.goto(0, 0)
        self.write("1", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()
        self.update_scoreboard()