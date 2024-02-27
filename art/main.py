# import colorgram as c

# extracted_color = c.extract('C:\\Users\\kushal cherukula\\Desktop\\projects 2024\\art\\spot_art.jpg',12)
# colors = []
# for i in extracted_color:
#     r = i.rgb.r
#     b = i.rgb.b
#     g = i.rgb.g
#     colors.append((r,g,b))

# print(colors)
from turtle import Turtle as t,Screen as s
from random import choice
import turtle

tim = t()
turtle.colormode(255)



color_list =[(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174)]
tim.up()
tim.hideturtle()
tim.speed(10)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_count = 100

for i in range(1,dot_count + 1):
    tim.dot(20,choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = s()
screen.exitonclick()