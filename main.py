import customtkinter as ctk
from customtkinter import *
from pass_entry import Cred
from Encryption import EnCrypt
from newUser import newUser

class CriptrApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cryption")
        self.setup_window()
        self.create_widgets()
        self.mainloop()

    def setup_window(self):
        window_width = 800
        window_height = 400
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        left = (display_width - window_width) // 2
        top = (display_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{left}+{top}")
        self.bind("<Escape>", lambda event: self.quit())

    def create_widgets(self):
        welcome_label = CTkLabel(
            self,
            text="Welcome to CRIPTR",
            font=CTkFont(family="<Arial>", size=30, weight="bold"),
            justify="center"
        )
        welcome_label.pack(pady=7)

        encrypt_button = CTkButton(
            self,
            text="Encryption",
            command=EnCrypt,
            cursor="target",
            font=CTkFont(family="<Arial>", size=25, weight="bold"),
            hover_color="dark blue"
        )
        encrypt_button.pack(side = TOP, pady=(90,0))

        decrypt_button = CTkButton(
            self,
            text="Decryption",
            command=self.open_credentials,
            cursor="pirate",
            font=CTkFont(family="<Arial>", size=25, weight="bold"),
            hover_color="dark green"
        )
        decrypt_button.pack(side = TOP, pady=30)

        new_user_button = CTkButton(
            self,
            text="New user ?",
            command=newUser,
            font=CTkFont(family="<Arial>", size=12),
            fg_color="transparent",
            hover=False,
            border_width=0
        )
        new_user_button.pack(side= "bottom")

    def open_credentials(self):
        Cred()

class Criptr:
    def __init__(self):
        CriptrApp()

if __name__ == "__main__":
    Criptr()