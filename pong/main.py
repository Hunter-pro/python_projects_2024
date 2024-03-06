from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.tracer(0)
screen.setup(height=600,width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.onkey(l_paddle.paddle_up,'w')
screen.onkey(l_paddle.paddle_down,'s')
screen.onkey(r_paddle.paddle_up,'Up')
screen.onkey(r_paddle.paddle_down,'Down')

game_is_on = True


     
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collison with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    
    
    #Detect the ball missed by r_paddle
    if ball.xcor() > 380:  
        ball.ball_reset()
        scoreboard.l_point()
        
    #Detect the ball missed by l_paddle
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()


    
    







screen.exitonclick()
