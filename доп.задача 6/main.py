import tkinter as tk 
from tkinter import ttk
from tkinter import NW
from tkinter import *
import re

def is_valid(newval):
    return re.match("^\d{0,3}$", newval) is not None

materials = ('Пластик', 'Аллюминий', 'Соломка', 'Текстиль')

win = tk.Tk()
win.geometry("500x300")
win.title('Жалюзи')

check = (win.register(is_valid), "%P")

label = Label(win, text="Ширина (см) ", anchor=NW)
label.place(x=20,y=30)

shirina = ttk.Entry(validate="key", validatecommand=check) 
shirina.place(x=120,y=30)

label = Label(win, text="Высота (см) ", anchor=NW)
label.place(x=20,y=60)

width = ttk.Entry(validate="key", validatecommand=check) 
width.place(x=120,y=60)

label = Label(win, text="Материалы", anchor=NW)
label.place(x=20,y=90)

combo = ttk.Combobox(win, values = materials)
combo.place(x=120,y=90)

btn = Button(win, text="Ok")
btn.place(x=20, y=120)

win.mainloop()