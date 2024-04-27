import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json

class newUser():

    def __init__(self):
        self.new = Tk()
        self.new.configure(bg="light blue")
        self.new.geometry("500x300")
        
        try:
            with open("user_data.json", "r") as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            self.data = {}

        Label(self.new, text="Set Username", bg="light blue", font="Arial 16 bold").pack(pady=7)
        self.user_entry = Entry(self.new)
        self.user_entry.pack(pady=7)

        Label(self.new, text="Set password", bg="light blue", font="Arial 16 bold").pack(pady=7)
        self.password_entry = Entry(self.new, width=20)
        self.password_entry.pack(pady=7)

        sub = Button(
            self.new,
            text="Submit",
            bg="blue",
            fg="white",
            font=23,
            activebackground="purple",
            command=self.save_new,
        )
        sub.pack(pady=10)

        self.new.bind('<Return>', self.save_new)
        self.new.mainloop()
        
    def save_new(self, event=None):
        username = self.user_entry.get()
        password = self.password_entry.get()

        if username and password:
            if username in self.data:
                messagebox.showerror("Error", "Username already exists!")
            else:
                self.data[username] = password
                messagebox.showinfo("Success", "User created successfully!")
                # Save updated data to JSON file
                with open("user_data.json", "w") as json_file:
                    json.dump(self.data, json_file)
                self.new.destroy()
        else:
            messagebox.showerror("Error","Please enter both username and password.")

newUser()