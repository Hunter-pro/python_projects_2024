
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Welcome to Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting the collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()
    
    #Detecting collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score.gameOver()

    #Detect collision with tail
    for turtle in snake.turtles[1:]:
        
        if snake.head.distance(turtle) < 10:
            #if collison with nay segment in the tail:
            game_is_on = False
            score.gameOver()


    
        
        
    


        
        


screen.exitonclick()