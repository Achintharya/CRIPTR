import tkinter as Tk
from tkinter import *
from trans_string import *

def DeCrypt():
    from pass_entry import username

    top2 = Tk()
    top2.title("DeCryption")
    top2.geometry("700x450")
    top2.configure(bg="light blue")
    
    welc_message = Label(top2, text = "Welcome "+username, font = ("Curlz MT", 20, "bold"), bg = "light blue").grid(row=0, column = 1, pady = (0,20))

    def exit2():
        return top2.destroy()

    def decode():

        decryptTransTable = str.maketrans(d, e)
        data2 = str(data2_entry.get())
        result = data2.translate(decryptTransTable)
        result_label.config(text=result)

    data2 = Label(
        top2, text="Enter data to Decrypt : ", font="Arial 16 bold", bg="light blue"
    ).grid(row=1, column=0)

    data2_entry = Entry(top2)
    data2_grid = data2_entry.grid(row=1, column=1)
    data2_button = Button(
        top2,
        text="Decode",
        command=decode,
        bg="pink",
        fg="navy blue",
    
        activebackground="green",
    ).grid(row=1, column=2)

    result_name = Label(
        top2, text="DeCrypted data : ", font="Arial 18 bold", bg="light blue"
    ).grid(row=2, column=0)
    result_label = Label(top2, bg="Light blue", font=10)
    result_label.grid(row=2, column=1)

    blah = Label(top2, font=16, bg="light blue").grid(row=4, column=2)
    
    exit2_button = Button(
        top2,
        text="Exit",
        command=exit2,
        bg="red",
        fg="white",
        activebackground="magenta",
        font=23,
    
    ).grid(row=5, column=2)