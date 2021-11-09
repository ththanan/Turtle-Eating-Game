from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")


class Rule(Turtle):

    def all_rules(self):
        self.penup()
        self.hideturtle()
        self.color("beige")
        self.goto(0, 60)
        self.write("Press button 'up', 'down', 'left' and 'right' to control the snake.", align=ALIGNMENT, font=FONT)


    def clear_rules(self):
        self.clear()