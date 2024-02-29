from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
bet_color = screen.textinput(title="make your bet",prompt="Which turtle will win the race?enter a color:")
colors = ['red','orange','violet','indigo','blue','green','yellow']
all_turtles = []
y = -100
for i in colors:
    new_turtle = Turtle('turtle')
    new_turtle.color(i)
    new_turtle.up()
    new_turtle.goto(x = -220,y = y)
    y += 30
    all_turtles.append(new_turtle)

if bet_color:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet_color:
                print(f"you've  won,The {winning_color} turtle is the winner")
            else:
                print(f"you've lost,the {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)





screen.exitonclick()