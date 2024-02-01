from turtle import Turtle
ALIGNMENT = "Center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.show_score()
