from turtle import Turtle
ALLIGNMENT = "center"
FONT = ('Courier', 18, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear
        self.write(f"Score:{self.score}   High Score: {self.high_score}", align=ALLIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALLIGNMENT, font=FONT)


