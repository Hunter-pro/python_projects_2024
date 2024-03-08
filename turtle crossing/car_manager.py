from random import randint,choice
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_speed_increase = MOVE_INCREMENT

    def create_car(self):
            random_chance = randint(1,6)
            if random_chance == 6:
                car = Turtle('square')
                car.shapesize(stretch_len=2,stretch_wid=1)
                car.color(choice(COLORS))
                car.up()
                car.goto(300,randint(-250,250))
                self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.back(self.move_speed)
        
    def car_speed_increase(self):
         self.move_speed += self.move_speed_increase
         

        
        

    

