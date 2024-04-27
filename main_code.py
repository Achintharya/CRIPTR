import tkinter as Tk
from tkinter import *
from pass_entry import Cred
from Decryption import DeCrypt
from Encryption import EnCrypt
from newUser import newUser

class Criptr():

    win = Tk()
    win.configure(bg="Cyan")
    win.geometry("600x400")
    win.title("Cryption")

    Welc_message = Label(win, text ="Welcome to CRIPTR", font="Arial 20 bold", bg="Cyan"
    ).pack(pady=7)

    but1 = Button(
        win,
        text="EnCryption",
        command=EnCrypt,
        cursor = "target",
        font="Helvetica 18 bold",
        bg="Teal",
        activebackground="light blue",
    ).pack(pady=35)
    
    but2 = Button(
        win,
        text="DeCryption",
        command=Cred,
        font="Helvetica 18 bold",
        cursor = "pirate",
        bg="Teal",
        activebackground="light blue",
    ).pack(pady=70)
    
    but3 = Button(win, text="New user ?", command = newUser, font="Helvetica 12", bg="cyan", activebackground="Cyan", border=0 ).pack()
    
    if __name__ == "__main__":
        win.mainloop()
        
