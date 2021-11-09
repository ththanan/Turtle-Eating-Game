from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from rule import Rule
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("DarkSlateGrey")
screen.title("Turtle Eating Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
rule = Rule()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

rule.all_rules()
scoreboard.countdown()
rule.clear_rules()

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 190 or snake.head.ycor() < -190:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
