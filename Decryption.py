import json
import customtkinter as Tk
from customtkinter import *
from tkinter import messagebox
from CustomMessagebox import show_custom_message

class DeCrypt(Tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DeCryption")
        self.setup_window()
        self.create_widgets_layout()
        self.load_hash_values()
        self.mainloop()
        
    def setup_window(self):
        window_width = 900
        window_height = 550
        left = (self.winfo_screenwidth() - window_width) // 2
        top = (self.winfo_screenheight() - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{left}+{top}")
        self.bind("<Escape>", lambda event: self.quit())

    def exit2(self):
        self.destroy()

    def decode(self):
        encoded_data = str(self.data_entry.get("1.0", "end-1c")).strip()
        decoded_data = ""
        errors = []

        if not encoded_data:
            show_custom_message(title="Input error", message="Enter text to decode", parent_x=900, parent_y=550)
            return

        for encoded_word in encoded_data.split(" "):
            components = encoded_word.strip().split("Ω")

            if len(components) >= 2:
                hash_value_str = components[1]

                if hash_value_str in map(str, self.hash_values.values()):
                    for word, hash_value in self.hash_values.items():
                        if str(hash_value) == hash_value_str:
                            decoded_data += word + " "
                            break
                else:
                    errors.append(f"Failed to decode word: {encoded_word}")
            else:
                errors.append(f"Invalid encoded word format: {encoded_word}")

        if errors:
            messagebox.showerror("Decryption Errors", "\n".join(errors))

        self.result_label.configure(text=decoded_data.strip())

    def load_hash_values(self):
        try:
            with open("HASH_VALUES.json", "r") as json_file:
                self.hash_values = json.load(json_file)
            print("Hash Values Loaded") 
        except FileNotFoundError:
            self.hash_values = {}
            show_custom_message(title="Error", message="Hash values file not found", parent_x=900, parent_y=550) 

    def create_widgets_layout(self):
        top_frame = CTkFrame(self, fg_color="transparent")
        mid_frame = CTkFrame(self, fg_color="transparent")
        bottom_frame = CTkFrame(self, fg_color="transparent")
        
        font = CTkFont(family="Arial", size=20, weight="bold")

        data_label = CTkLabel(top_frame, text="Enter data to Decode : ", font=font)
        self.data_entry = CTkTextbox(top_frame, height=200, width=400)
        decode_button = CTkButton(top_frame, text="Decode", command=self.decode, hover_color="green")
        result_name = CTkLabel(mid_frame, text="Decoded data : ", font=font)
        self.result_label = CTkLabel(mid_frame, text="Wait for it", font=CTkFont(family="Arial", size=12, slant="italic"))
        exit_button = CTkButton(bottom_frame, text="Exit", command=self.exit2, hover_color="red")
        
        top_frame.pack(side="top", pady=10)
        mid_frame.pack(side="top", pady=20)
        bottom_frame.pack(side="bottom")

        data_label.pack(side="left")
        self.data_entry.pack(padx=10)
        decode_button.pack(padx=10)
        result_name.pack(side="left", pady=10)
        self.result_label.pack(side="left", pady=10)
        exit_button.pack()