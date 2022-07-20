from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.x_score=0
        self.y_score=0
        self.goto(x=0,y=230)
        self.write_f()
    
    def inscrease(self):
        self.clear()
        self.write_f()
    def write_f(self):
        self.write(f"{self.x_score}       {self.y_score}", align='center', font=('Courier', 50, 'normal'))
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", align='center',font=('Arial', 30,"normal"))