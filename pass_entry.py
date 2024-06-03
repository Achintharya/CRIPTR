import customtkinter as ctk
from customtkinter import *
from tkinter.messagebox import showerror
from Decryption import DeCrypt
import json


class Cred(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.data = {}  # Initialize self.data here
        self.setup_window()
        self.read_user_data()
        self.mainloop()        
    
    def setup_window(self):
        window_width = 500
        window_height = 300
        left = (self.winfo_screenwidth() - window_width) // 2
        top = (self.winfo_screenheight() - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{left}+{top}")
        self.bind("<Escape>", lambda event: self.destroy())
        self.attributes("-topmost", True)
        
        CTkLabel(self, text="Enter Username").pack(pady=7)
        self.user = CTkEntry(self)
        self.user.pack(pady=7)

        CTkLabel(self, text="Enter password").pack(pady=7)
        self.password = CTkEntry(self, show="*")
        self.password.pack(pady=7)

        CTkButton(
            self,
            text="Submit",
            command=self.close_win,
        ).pack(pady=10)
        self.bind('<Return>', self.close_win)
    
    def read_user_data(self):
        try:
            with open("user_data.json", "r") as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass  # Do nothing if the file is not found

    def close_win(self, event=None):
        username = self.user.get()
        password = self.password.get()
        if not username or not password:
            showerror("ERROR", "Please enter both username and password.")
            return
        for key, value in self.data.items():
            if key == username:
                if value == password:
                    self.destroy()
                    DeCrypt()
                    return
                else:
                    showerror("ERROR", "Wrong password")
                    return
        showerror("ERROR", "Wrong username")

if __name__ == "__main__":
    Cred().mainloop()