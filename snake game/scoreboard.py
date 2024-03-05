
from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Arial',15,'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.score = 0
        self.goto(0,270)
        self.write(f'Score: {self.score}',align=ALIGNMENT,font=FONT)
        self.ht()
    
    def gameOver(self):
        self.goto(0,0)
        self.write('GAME OVER',align=ALIGNMENT,font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}',align=ALIGNMENT,font=FONT)