from turtle import Screen
from Snake_class import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    if snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.xcor()<-290 or snake.head.ycor()>290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.all_snake_part[1:]:
        if snake.head.distance(segment)<7:
            scoreboard.reset()
             

screen.mainloop()


