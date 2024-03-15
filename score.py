from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score: {self.score}", False, align="center", font=("Garamond", 16, "normal") )
   
        
    def add_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", False, align="center", font=("Garamond", 16, "normal") )

   
    def you_lose(self):
        self.goto(0,0)
        self.write("You Lose.", False,align="center",font=("Garamond", 16, "normal"))
        