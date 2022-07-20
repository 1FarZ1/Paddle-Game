from turtle import Turtle 
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed("fastest")
        self.y_mov=10
        self.x_mov=10
    def move(self):
        x=self.xcor()
        y=self.ycor()
        self.goto(x+self.x_mov,y+self.y_mov)
    def bounce(self):
        self.y_mov=-self.y_mov
    def bounce_paddle(self):
        self.x_mov*= -1
       ## u can also develeop the speed  To do
    def spawn(self):
        self.goto(0,0)
        self.bounce_paddle()
        