from tkinter import *
from PIL import ImageTk, Image

imgMorte = None
vida = None

def morte(my_label):
    #destruir todos os widgets/limpar a tela
    for widget in root.winfo_children():
        widget.destroy()
    global imgMorte 
    imgMorte = ImageTk.PhotoImage(Image.open("images/morte.png"))
    telaMorte = Label(image=imgMorte)
    telaMorte.grid(row=0, column=0)

def vida(my_label):
    for widget in root.winfo_children():
        widget.destroy()
    global imgVida
    imgVida = ImageTk.PhotoImage(Image.open("images/vida.png"))
    telaVida = Label(image=imgVida)
    telaVida.grid(row=0, column=0)
    


root = Tk()
root.title('Learn Tkinter')
my_img = ImageTk.PhotoImage(Image.open("images/ladrao.png"))
my_label = Label(image=my_img)
my_label.grid()


Labeltxt1 = Label(root, text="O dinheiro ou a vida ?")
button1 = Button(root, text="Dar dinheiro", command=lambda:vida(my_label))
button2 = Button(root, text="Nao dar dinheiro", command=lambda: morte(my_label))
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

root.mainloop()