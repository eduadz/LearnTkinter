from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')

my_image1 = ImageTk.PhotoImage(Image.open("images/ladrao.png").resize([500,500]))
my_image2 = ImageTk.PhotoImage(Image.open("images/ladrao2.png").resize([500,500]))
my_image3 = ImageTk.PhotoImage(Image.open("images/ladrao3.png").resize([500,500]))

image_list = [my_image1, my_image2, my_image3]

inicio = Label(text="Escolha o seu ladrao")
inicio.grid(row=0, column=1)
status = Label(text="Image 1 of "+ str(len(image_list)), bd=1, relief=SUNKEN) #colocar borda(bd) e deixar afundado (sunken)

label_img = Label(image=my_image1)
label_img.grid(row=1, column=0, columnspan=3)

def back(image_number):
    global label_img
    global button_forward
    global button_back

    label_img.grid_forget()
    label_img = Label(image=image_list[image_number-1])

    button_back = Button(root, text="<<", command= lambda: back(image_number-1))
    button_forward = Button(root, text=">>", command= lambda: forward(image_number+1))
    
    # Update Status Bar
    status = Label(text="Image "+ str(image_number) +" of "+ str(len(image_list)), bd=1, relief=SUNKEN) 
    status.grid(row=3, column=0, columnspan=3, sticky=W+E) 
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label_img.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=2, column=0)


def forward(image_number):
    global label_img
    global button_forward
    global button_back

    label_img.grid_forget()
    label_img = Label(image=image_list[image_number-1])

    button_back = Button(root, text="<<", command= lambda: back(image_number-1))
    button_forward = Button(root, text=">>", command= lambda: forward(image_number+1))
    
    # Update Status Bar
    status = Label(text="Image "+ str(image_number) +" of "+ str(len(image_list)), bd=1, relief=SUNKEN) 
    status.grid(row=3, column=0, columnspan=3, sticky=W+E) 
    
    if image_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED)

    label_img.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)



button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text=" EXIT ", command= root.quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))

button_back.grid(row=2, column=0)
button_exit.grid(row=2, column=1, pady= 10)
button_forward.grid(row=2, column=2)
status.grid(row=3, column=0, columnspan=3, sticky=W+E) #sticky estica de West à East

root.mainloop()