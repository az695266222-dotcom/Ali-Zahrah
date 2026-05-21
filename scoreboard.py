from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.highscore = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt","r") as file:
            return int(file.read())

    def save_highscore(self):
        with open ("highscore.txt", "w") as file:
            file.write(str(self.highscore))




    def update_scoreboard(self):
        self.write(f"Score: {self.score}       High score: {self.highscore}",align="center", font=("courier",24,"bold"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.clear()
        self.screen.bgcolor('#800080')
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.pencolor("#00A028")
        self.write(f"----------Game Over----------\n\nFinal Score: {self.score}\n\n High Score: {self.highscore}",align="center", font=("courier",24,"bold"))
        