from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#Definindo um frame
frame1 = LabelFrame(text="Frame", padx=20, pady=20)
frame1.grid(row=0,column=0,padx=10, pady=10)

frame2 = LabelFrame(padx=20, pady=20)
frame2.grid(row=0,column=1,padx=10, pady=10)

b1 = Button(frame1,text= "Click me")
b2 = Button(frame1,text= "Click here too")
b3 = Button(frame2,text= "Click me")
b1.grid(row=0, column=1)
b2.grid(row=1, column=1)
b3.pack()

root.mainloop()
