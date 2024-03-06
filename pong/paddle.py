from tkinter import Y
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.up()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def paddle_up(self):
        cor_y = self.ycor() +20
        self.goto(self.xcor(),y=cor_y)
    
    def paddle_down(self):
        cor_y = self.ycor() -20
        self.goto(self.xcor(),y=cor_y)



    
    