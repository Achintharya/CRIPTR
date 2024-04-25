from tkinter import *
from tkinter import messagebox
from DeCrypt import * 


class Cred:
    def __init__(self):
        self.cre = Tk()
        self.cre.configure(bg="light blue")
        self.cre.geometry("500x300")

        Label(self.cre, text="Enter Username", bg="light blue", font="Arial 16 bold").pack(pady=7)
        self.user = Entry(self.cre)
        self.user.pack(pady=7)

        Label(self.cre, text="Enter password", bg="light blue", font="Arial 16 bold").pack(pady=7)
        self.password = Entry(self.cre, show="*", width=20)
        self.password.pack(pady=7)

        sub = Button(
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
        username = self.user.get()
        password = self.password.get()
        for key, value in user_pass.items():
            if key == username:
                if value == password:
                    DeCrypt()             
                    self.cre.destroy()
                    return
                else:
                    messagebox.showerror("ERROR", "Wrong password")
                    return
        messagebox.showerror("ERROR", "Wrong username")

# User credentials
user_pass = {"Achintharya": "0615", "Arav": "2604", "Arun": "1307"}