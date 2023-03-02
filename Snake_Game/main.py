from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#screen creation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
SCORE = 0

#turtle creation
snake = Snake()
#food creation
food = Food()
#Scoreboard creation
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.add_score(SCORE)





screen.exitonclick()