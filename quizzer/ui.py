THEME_COLOR = "#375362"

from tkinter import Tk,Label,Canvas,PhotoImage,Button

import comm
from quiz_brain import QuizBrain

class QuizeUi:
    def __init__(self,quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.window.title('Quizzler')

        self.label= Label(text=f"Score = {self.quiz.score}",background=THEME_COLOR,font=('Arial',20,'bold'))
        self.label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.text = self.canvas.create_text(150,125,text='Question',fill=THEME_COLOR,font=('Arial',20,'italic'),width=280)

        true_image = PhotoImage(file='./quizzer/images/true.png')
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.correct)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file='./quizzer/images/false.png')
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.wrong)
        self.false_button.grid(row=2,column=1)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text,text=q_text)

    def correct(self):
        is_right = self.quiz.check_answer('True')
        self.givefeedback(is_right)
    
    def wrong(self):
        is_right = self.quiz.check_answer('False')
        self.givefeedback(is_right)
    
    def reset(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.next_question()
        else:
            self.canvas.itemconfig(self.text,text=f'Your Final score is {self.quiz.score}/10')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def givefeedback(self,is_right:bool):
        if is_right:
            self.canvas.config(bg='green')
            self.label.config(text=f'Score = {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.reset)


    