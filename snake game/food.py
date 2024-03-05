from turtle import Turtle, ycor
import random 
COLORS = ['violet','yellow','blue','white','purple','red','indigo']
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280,280)
        self.goto(x_cor,y_cor)