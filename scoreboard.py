from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial" , 22 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.update_score()    
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")

        self.score=0
        self.update_score()    



    def increse_score(self):
        self.score+=1
        self.clear()
        self.update_score()

