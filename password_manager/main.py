from tkinter import PhotoImage
from altair import Padding
from customtkinter import CTkCanvas,CTk,CTkLabel,CTkEntry,CTkButton,END
from tkinter import messagebox
#---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip


def password_generator():
    password = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(symbols) for char in range(nr_symbols)]+[random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    if password != '':
        password_entry.delete(0,END)

    password_entry.insert(0,string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_passwords():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if email=='' or password == '':
        messagebox.showerror(message='please don\'t leave any field empty')
    
    else:
        confirm = messagebox.askokcancel(title=website,message=f'These are the details you have entered \nemail:{email}\npassword:{password}')

        if confirm:
            with open('./password_manager/passwords',mode='+a') as file:
                details = f"\n\nemail:{email}\nwebsite:{website}\npassword:{password}"
                file.write(details)
            website_entry.delete(0,END)
            password_entry.delete(0,END)


    


# ---------------------------- UI SETUP ------------------------------- #

window = CTk()
window.title('password manager')
window.configure(padx=50,pady=50)


canvas = CTkCanvas(window,width=200,height=200,bg='#242424',highlightthickness=0)
logo = PhotoImage(file='./password_manager/logo.png')
canvas.create_image(100,100,image=logo,)
canvas.grid(row=0,column=1)

website_label = CTkLabel(window,text='Website',text_color='#f1f1f1')
website_label.grid(row=1,column=0)

username_label = CTkLabel(window,text='Username/Email',text_color='#f1f1f1')
username_label.grid(row=2,column=0)

password_label = CTkLabel(window,text='Password',text_color='#f1f1f1')
password_label.grid(row=3,column=0)

website_entry = CTkEntry(window,width=350)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()


email_entry = CTkEntry(window,width=350)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'kushalcherukula@gmail.com')

password_entry = CTkEntry(window,width=210)
password_entry.grid(row=3,column=1)

generate_button = CTkButton(window,text='generate',command=password_generator)
generate_button.grid(row=3,column=2)

add_button = CTkButton(window,text='add',width=360,command=add_passwords)
add_button.grid(row=4,column=1,columnspan=2)








window.mainloop()
