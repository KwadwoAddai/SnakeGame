from turtle import Screen, Turtle
from snake import Snake
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
ball = Ball()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(ball) < 15:
        ball.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 15:
            score.reset()
            snake.reset()





screen.exitonclick()