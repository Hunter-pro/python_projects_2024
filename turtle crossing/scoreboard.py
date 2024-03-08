
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.up()
        self.ht()
        self.update_level()
        
    
    def update_level(self):
        self.level+=1
        self.clear()
        self.goto(-280,250)
        self.write(f'Level:{self.level}',font=FONT,align='left')

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',font=FONT,align='center')
    



