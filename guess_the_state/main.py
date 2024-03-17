from turtle import  Turtle,Screen
import turtle
from retrive_data import Data


screen = Screen()
data = Data()
pen = Turtle()
pen.ht()
pen.up()


screen.title('US states Game')

#setting the map to background
image = './guess_the_state/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

score = 0
no_of_states = 50
tries = 0


game_is_on = True
while game_is_on:
    if score == 0:
        title = 'Guess the state'
        prompt = 'Enter the state name'
    else:
        title = f'score:{score}/{no_of_states}'
        prompt = 'Enter the next state'


    user_ans = screen.textinput(title=title, prompt=prompt)
    user_ans = str(user_ans).title()

    if data.check_state(user_ans):
        score+=1
        pen.goto(data.cord_dict[user_ans])
        pen.write(f'{user_ans}')
    else:
        tries += 1
        print(tries)
    
    if tries == 5:
        data.create_missed()
        game_is_on = False
    

    

    

    


    






turtle.mainloop()