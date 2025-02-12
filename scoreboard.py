from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=150, y=250)
        self.write(f"Level:{self.level}", True, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=150, y=250)
        self.write(f"Level:{self.level}", True, font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write("Game Over!", True, font=FONT)