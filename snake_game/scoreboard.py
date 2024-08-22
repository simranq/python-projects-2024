from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
       #file read,write  operations are used over here so that the last highscore entry is maintained
        # well and saved for further gameplay even after reinitiating the whole game again
        with open("data") as data:
            self.highscore = int(data.read())
        #self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        with open("data",'w') as data:
            data.write(f"{self.highscore}")


    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score=0
        self.update_scoreboard()
    '''
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

   '''
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
