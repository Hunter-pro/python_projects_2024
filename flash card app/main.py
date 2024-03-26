BACKGROUND_COLOR = "#B1DDC6"
import random
from tkinter import Button, PhotoImage, Tk,Canvas
from turtle import bgcolor

import pandas
try:
    data = pandas.read_csv('./flash card app/data/words_to_learn.csv')
except:
    originaldata = pandas.read_csv('./flash card app/data/french_words.csv')
    records = originaldata.to_dict(orient="records")
else:
    records = data.to_dict(orient="records")
    

words_to_learn = records
new_word = {}

#-----------------------------CHANGE TEXT WORDS------------------------------#
def change_words_wrong(): 
    global new_word,flip
    window.after_cancel(flip)
    new_word = random.choice(records)
    canvas.itemconfig(word,text=new_word['French'],fill='black')
    canvas.itemconfig(title,text='French',fill='black')
    canvas.itemconfig(card_image,image=front_image)
    flip = window.after(3000,flip_card)

#-----------------------------FLIP CARD--------------------------------------#
def flip_card():
    global new_word
    
    canvas.itemconfig(card_image,image=back_photo)
    canvas.itemconfig(title,text='English',fill='white')
    canvas.itemconfig(word,text=new_word['English'],fill = 'white')
    canvas.itemconfig(card_image,image=back_photo)

def change_words_correct():
    change_words_wrong()
    words_to_learn.remove(new_word)
    




#-------------------------------UI SETUP--------------------------------------#

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip = window.after(3000,flip_card)

canvas = Canvas(window,width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2)

front_image = PhotoImage(file='./flash card app/images/card_front.png')
card_image = canvas.create_image(400,263,image=front_image)
title = canvas.create_text(400,150,text='Title',font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text='word',font=("Ariel",60,"bold"))
 

correct_img = PhotoImage(file='./flash card app/images/right.png')
correct_button = Button(image=correct_img,highlightthickness=0,command=change_words_correct)
correct_button.grid(row=1,column=0)

wrong_img = PhotoImage(file='./flash card app/images/wrong.png')
wrong_button = Button(image=wrong_img,highlightthickness=0,command=change_words_wrong)
wrong_button.grid(row=1,column=1)

back_photo = PhotoImage(file='./flash card app/images/card_back.png')

change_words_wrong()


window.mainloop()

new_words = pandas.DataFrame(words_to_learn)
new_words.to_csv('./flash card app/data/words_to_learn.csv',index=False)