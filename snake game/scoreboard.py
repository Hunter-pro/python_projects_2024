
from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Arial',15,'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.score = 0
        with open(r'C:\Users\kushal cherukula\Desktop\projects 2024\snake game\data.txt',mode='r') as file:
            self.high_score = int(file.read())
        self.goto(0,270)
        self.ht()
        self.score_update()

    
    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER',align=ALIGNMENT,font=FONT)
        

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open(r'C:\Users\kushal cherukula\Desktop\projects 2024\snake game\data.txt',mode='w') as file:
                file.write(f'{self.high_score}')

        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}',align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_update()