from token import STAR
from turtle import Turtle



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.up()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    
    def move_up(self):
        self.fd(MOVE_DISTANCE)


    def reposition(self):
        self.goto(STARTING_POSITION)        
