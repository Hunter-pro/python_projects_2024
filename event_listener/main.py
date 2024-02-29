from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(rotate_left,'a')
screen.onkey(rotate_right,'d')
screen.onkey(clear,'c')
screen.exitonclick()