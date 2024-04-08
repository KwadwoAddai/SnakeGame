from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.pu()
        self.goto(0, 260)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} || HighScore: {self.highscore}", align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.color('red')
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 30, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()


