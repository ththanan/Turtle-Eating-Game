from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(name="turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("LightGoldenrod")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-120, 120)
        self.goto(random_x, random_y)
