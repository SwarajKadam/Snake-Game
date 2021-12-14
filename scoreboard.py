from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.score =0
        file =open("data.txt","r")        
        self.highscore =int(file.read())
        file.close()
        self.goto(0,268)
        self.color("white")
        self.hideturtle()
        self.write(arg =f"Score :{self.score} High Score{self.highscore}", align="center",font=("Arial",24,"normal"))
        

    def increment_point(self):
        self.score +=1
        self.clear()
        self.write(arg =f"Score :{self.score} High Score{self.highscore}", align="center",font=("Arial",24,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg ="GAME OVER ", align="center",font=("Arial",24,"normal"))   
        
    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.increment_point() 
        