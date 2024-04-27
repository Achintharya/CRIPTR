import tkinter as Tk
from tkinter import *
from pass_entry import *
from DeCrypt import *
from EnCrypt import *

class Criptr():

    win = Tk()
    win.configure(bg="Cyan")
    win.geometry("600x400")
    win.title("Cryption")

    Welc_message = Label(win, text ="Welcome to CRIPTR", font="Arial 20 bold", bg="Cyan"
    ).pack(pady = 20)

    but1 = Button(
        win,
        text="EnCryption",
        command=EnCrypt,
        cursor = "target",
        font="Helvetica 18 bold",
        bg="Teal",

        activebackground="light blue",
    ).pack(pady = 40)
    but2 = Button(
        win,
        text="DeCryption",
        command=Cred,
        font="Helvetica 18 bold",
        cursor = "pirate",
        bg="Teal",

        activebackground="light blue",
    ).pack()
    
    if __name__ == "__main__":
        win.mainloop()
        