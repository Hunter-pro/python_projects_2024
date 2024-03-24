from tkinter import PhotoImage
from altair import Padding
from customtkinter import CTkCanvas,CTk,CTkLabel,CTkEntry,CTkButton,END
from tkinter import messagebox
#---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json


def password_generator():
   
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
    email = email_entry.get() #getting the contents for entry usin get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {website:          #converting the data into a json dict format ie dict(dict)
                {
                    "email":email,
                    "password":password
                }
    }

    if email=='' or password == '':#checking if the password field is empty
        messagebox.showerror(message='please don\'t leave any field empty')
    
    else:#password is not empty
        try:
            with open('./password_manager/password.json',mode='r') as file: #open a json file in read mode
                data = json.load(file)  # try read or get the data from json file
        except:
            with open('./password_manager/password.json',mode='w') as file:
                json.dump(new_data,file,indent=4) # if file is not found or no entries ie first time running create the file
        else:
            data.update(new_data)# if the json file exist then update the data read

            with open('./password_manager/password.json',mode='w') as file: # now update the data into json file
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0,END)# after saving or writing into json file clear the entries
            password_entry.delete(0,END)

# ------------------------ SEARCH FUNCTION --------------------------- #
def search_website():
    website = website_entry.get()
    
    try:
        with open('./password_manager/password.json','r') as file:
            data = json.load(file)     
        website_data = data[website]
    except KeyError:
        messagebox.showerror(message='Website details not found',title='error')
    except FileNotFoundError:
        messagebox.showerror(message='No Data file found')
    else:
        email = website_data['email']
        password = website_data['password']
        messagebox.showinfo(title='info',message=f'email:{email}\npassword:{password}')



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

website_entry = CTkEntry(window,width=210)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()


email_entry = CTkEntry(window,width=350)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'kushalcherukula@gmail.com')

password_entry = CTkEntry(window,width=210)
password_entry.grid(row=3,column=1)

generate_button = CTkButton(window,text='generate',command=password_generator)
generate_button.grid(row=3,column=2)

search_button = CTkButton(window,text='Search',command=search_website)
search_button.grid(row=1,column=2)

add_button = CTkButton(window,text='add',width=360,command=add_passwords)
add_button.grid(row=4,column=1,columnspan=2)








window.mainloop()
