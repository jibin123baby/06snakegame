from turtle import Turtle

FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setposition(0.0, 280.0)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score is {self.score}", move=False, align='center', font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("Game Over", move=False, align='center', font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()