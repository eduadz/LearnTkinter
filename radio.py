from tkinter import *
from PIL import ImageTk, Image

root = Tk()

r = IntVar()

MODES = [# ("name on screen", "value")
    ("Calabresa", "Calabresa"), 
    ("4 queijos", "4 queijos"),
    ("Portuguesa", "Portuguesa"),
    ("Milho", "Milho"),
]

pizza = StringVar()

#create a loop for radioButtons
for text,value in MODES:    
    Radiobutton(text=text,variable=pizza ,value=value).pack()


def att(value):
    mylabel = Label(text=value)
    mylabel.pack()

#Radiobutton(text="Option 1", variable=r, value=1,command=lambda: att(r.get())).pack()
#Radiobutton(text="Option 2", variable=r, value=2,command=lambda: att(r.get())).pack()

#mylabel = Label(text=r.get())
#mylabel.pack()

bt = Button(text="Click me", command=lambda:att(pizza.get()))
bt.pack()

mainloop()