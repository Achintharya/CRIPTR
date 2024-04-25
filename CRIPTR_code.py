import tkinter as Tk
from tkinter import *
import os
from pass_entry import *
from DeCrypt import *
from EnCrypt import *


class Criptr():

    win = Tk()
    win.configure(bg="Cyan")
    win.geometry("400x300")
    win.title("Cryption")


    e = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = "▲▼◀▶◢◣◥◤╰╯╭╮◄►▬↑↓↕→←↔♂♀♪♫☼§↨♥♦♣♠•○τΩδ∞φε∩╥╠╣╬╩╦╪╫╙╔╗"

    but1 = Button(
        win,
        text="EnCryption",
        command=EnCrypt,
        font="Helvetica 18 bold",
        bg="Teal",

        activebackground="light blue",
    ).pack(pady=60)
    but2 = Button(
        win,
        text="DeCryption",
        command=Cred,
        font="Helvetica 18 bold",
        bg="Teal",

        activebackground="light blue",
    ).pack()

    if __name__ == "__main__":
        win.mainloop()
    