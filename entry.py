from tkinter import *
#the secret is define and pack

root = Tk()

e = Entry(root)
e.pack()


def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


myButton = Button(root, text="Submit", command=myClick, fg="white", bg="black")
myButton.pack()

root.mainloop()


