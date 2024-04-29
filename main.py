import tkinter as Tk
from tkinter import *
from pass_entry import Cred
from Decryption import DeCrypt
from Encryption import EnCrypt
from newUser import newUser


class Criptr():

    win = Tk()
    win.configure(bg="Cyan")
    win.geometry("800x450")
    win.title("Cryption")

    Welc_message = Label(win, text ="Welcome to CRIPTR ", font="Helvetica 20 bold", bg="Cyan", justify="center"
    ).pack(pady=7)

    but1 = Button(
        win,
        text="Encryption",
        command=EnCrypt,
        cursor = "target",
        font="Helvetica 18 bold",
        bg="Teal",
        activebackground="light blue",
    ).pack(pady=35)
    
    but2 = Button(
        win,
        text="Decryption",
        command=Cred,
        font="Helvetica 18 bold",
        cursor = "pirate",
        bg="Teal",
        activebackground="light blue",
    ).pack(pady=70)
    
    but3 = Button(win, text="New user ?", command = newUser, font="Helvetica 12", bg="cyan", activebackground="Cyan", border=0 ).pack()
    
    if __name__ == "__main__":
        win.mainloop()