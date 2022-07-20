from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,start):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(start)
    def move_forward(self):
        self.setheading(90)
        self.forward(20)
        self.setheading(0)
    def move_backward(self):
        self.setheading(90)
        self.backward(20)
        self.setheading(0)