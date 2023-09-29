from tkinter import *
#the secret is define and pack

root = Tk()

#create label widget - define
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Eduardo Soares")


myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()


