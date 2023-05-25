import tkinter as tk 
from tkinter import ttk
from tkinter import NW
from tkinter import *
import re

def is_valid(newval):
    return re.match("^\d{0,5}$", newval) is not None

win = tk.Tk()
win.geometry("500x300")
win.title('Цифровая фотография')

check = (win.register(is_valid), "%P")

label = Label(win, text="Формат", anchor=NW)
label.place(x=20,y=30)

rb1 = Radiobutton(win, text='9 x 12', value=1)
rb1.place(x=20,y=50)

rb2 = Radiobutton(win, text='10 x 15', value=2)
rb2.place(x=20,y=70)

rb3 = Radiobutton(win, text='18 x 24', value=3)
rb3.place(x=20,y=90) 

label = Label(win, text="Колличество:", anchor=NW)
label.place(x=20,y=120)

count = ttk.Entry(validate="key", validatecommand=check) 
count.place(x=120,y=120)

btn = Button(win, text="Ok")
btn.place(x=20, y=150)

win.mainloop()