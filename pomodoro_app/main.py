
from tkinter import PhotoImage
from customtkinter import CTk,CTkCanvas,CTkButton,CTkLabel
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.configure(text='Break',text_color=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.configure(text='Break',text_color=PINK)
        ticks = ''
        for i in range(floor(reps/2)):
            ticks += '✔'
        tick.configure(text=ticks)
    
    else:
        count_down(work_sec)
        label.configure(text='work',text_color=GREEN)

    


    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = '0'+str(count_sec)

    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

# ---------------------------- TIMER RESET ------------------------------- # 
        
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text,text='00:00')
    label.configure(text='Timer')
    tick.configure(text='')
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #

window = CTk()
window.title('Pomodoro')
window.configure(padx=100,pady=50)

canvas = CTkCanvas(window,width=200,height=230,bg='#242424',highlightthickness=0)
tomato_photo = PhotoImage(file='./pomodoro_app/tomato.png')
canvas.create_image(100,115,image=tomato_photo)
timer_text = canvas.create_text(100,130,text='00:00',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)


label = CTkLabel(window,text='Timer',font=(FONT_NAME,50,'bold'),text_color=GREEN)
label.grid(row=0,column=1)

start_button = CTkButton(window,text='start',width=50,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = CTkButton(window,text='reset',width=50,command=reset_timer)
reset_button.grid(row=2,column=2)


tick = CTkLabel(window,text='',text_color=GREEN)
tick.grid(row=3,column=1)






window.mainloop()