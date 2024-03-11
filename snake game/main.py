
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

#asks user input to continue or discontiue the game
def continue_game():
    u_choice = None
    while u_choice not in ['yes', 'no']:
        u_choice = screen.textinput(title='MENU', prompt='Do you want to play again? Please enter yes or no:')
    if u_choice == 'yes':
        return True
    else:
        return False
    


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting the collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    #Detecting collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        if continue_game():
            score.reset()
            snake.reset()
            screen.listen()
        else:
            game_is_on = False

    #Detect collision with tail
    for turtle in snake.turtles[1:]:
        
        if snake.head.distance(turtle) < 10:
            #if collison with nay segment in the tail:
            if continue_game():
                score.reset()
                snake.reset()
                screen.listen()
            else:
                game_is_on = False

                


    
        
        
    


        
        


screen.exitonclick()