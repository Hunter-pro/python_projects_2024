import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()




screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen() 
screen.onkey(player.move_up,'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.car_move()
    
    for car in carmanager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False



    if player.ycor() >= 280:
        scoreboard.update_level()
        carmanager.car_speed_increase()
        player.reposition()
    

screen.exitonclick()
