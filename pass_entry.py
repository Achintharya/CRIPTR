import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Decryption import DeCrypt
import json

class Cred():
    def __init__(self):
        lb = "light blue"
        self.cre = Tk()
        self.cre.configure(bg=lb)
        self.cre.geometry("500x300")
        
        try:
            with open("user_data.json", "r") as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            self.data = {}

        Label(self.cre, text="Enter Username", bg=lb, font="Arial 16 bold").pack(pady=7)
        self.user = Entry(self.cre)
        self.user.pack(pady=7)

        Label(self.cre, text="Enter password", bg=lb, font="Arial 16 bold").pack(pady=7)
        self.password = Entry(self.cre, show="*", width=20)
        self.password.pack(pady=7)

        Button(
            self.cre,
            text="Submit",
            bg="blue",
            fg="white",
            font=23,
            activebackground="purple",
            command=self.close_win,
        ).pack(pady=10)
        self.cre.bind('<Return>', self.close_win)
        self.cre.mainloop()

    def close_win(self, event=None):
        global username
        username = self.user.get()
        password = self.password.get()
        if not username or not password:
            messagebox.showerror("ERROR", "Please enter both username and password.")
            self.cre.destroy()
            return
        for key, value in self.data.items():
            if key == username:
                if value == password:
                    DeCrypt()             
                    self.cre.destroy()
                    return
                else:
                    messagebox.showerror("ERROR", "Wrong password")
                    self.cre.destroy()
                    return
        messagebox.showerror("ERROR", "Wrong username")
        self.cre.destroy()

