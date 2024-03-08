
from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Arial',15,'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.score = 0
        self.high_score = 0
        self.goto(0,270)
        self.ht()
        self.score_update()

    
    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER',align=ALIGNMENT,font=FONT)
        

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}',align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_update()