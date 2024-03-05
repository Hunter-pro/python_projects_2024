from ctypes import pointer
from turtle import Turtle
POSITIONS_LIST = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =  0


class Snake:
    def __init__(self) -> None:
        self.turtles = []
        self.snake_create()
        self.head = self.turtles[0]

    def snake_create(self):
        for i in POSITIONS_LIST:
            self.add_segment(i)
          

    def move(self):
        for seg_num in range(len(self.turtles)-1,0,-1):
            new_x=self.turtles[seg_num -1].xcor()
            new_y=self.turtles[seg_num -1].ycor()
            self.turtles[seg_num].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)
    
    def down(self):
        if self.head.heading() != UP:  
            self.head.setheading(DOWN) 
        
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self,position):
        tim = Turtle('square')
        tim.color('white')
        tim.up()
        tim.goto(position)
        self.turtles.append(tim)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

        
    