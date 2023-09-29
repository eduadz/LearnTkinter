from tkinter import *
#the secret is define and pack

root = Tk()

def myClick():
    myLabel = Label(root, text="Penis")
    myLabel.pack()


myButton = Button(root, text="Click me", command=myClick, fg="white", bg="black")
myButton.pack()

root.mainloop()


