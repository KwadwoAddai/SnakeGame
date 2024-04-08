from turtle import Turtle
POS = [(40, 0), (20, 0), (0, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]
        self.head.color('red')

    def create_body(self):
        for snake_part in POS:
            self.add_body(snake_part)

    def add_body(self, snake_part):
        snake = Turtle('square')
        snake.color('white')
        snake.pu()
        snake.goto(snake_part)
        self.snake_body.append(snake)

    def reset(self):
        for body_part in self.snake_body:
            body_part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_body()
        self.head = self.snake_body[0]
        self.head.color('red')

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for snake_part in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[snake_part-1].xcor()
            new_y = self.snake_body[snake_part-1].ycor()
            self.snake_body[snake_part].goto(new_x, new_y)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



