from customtkinter import CTk, CTkLabel, CTkButton,CTkEntry
from panel import Row
from sqlalchemy import column

window = CTk()
window.title('Mile to km convertor')
window.minsize(width=250,height=200)
window.configure(padx=70,pady=70)

input = CTkEntry(window,width=75)
input.grid(row=0,column=1)


label1 = CTkLabel(window,text='Miles')
label1.grid(row=0,column=2)
label1.configure(padx=10)

label2 = CTkLabel(window,text='is Equal to')
label2.grid(row=1,column=0)
label2.configure(padx=10)

label3 = CTkLabel(window,text='0')
label3.grid(row=1,column=1)
label3.configure(padx=40)

label4 = CTkLabel(window,text='KM')
label4.grid(row=1,column=2)
label4.configure(padx=10)

def convertMilesToKm():
    miles = input.get()
    km = int(miles) * 1.60934
    label3.configure(text="{:.2f}".format(km))


button = CTkButton(window,text='Calculate',width=50,command=convertMilesToKm)
button.grid(row=2,column=1)















window.mainloop()