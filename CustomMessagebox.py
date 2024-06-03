import threading
import customtkinter as ctk

class CustomMessageBox(ctk.CTkToplevel):
    def __init__(self, master, title="Message", message="", parent_x=0, parent_y=0):
        super().__init__(master)
        self.title(title)
        window_width= 250
        window_height= 150
        self.setup_window(window_width, window_height, parent_x,parent_y)
        self.create_widgets(message)
        
    def setup_window(self, window_width, window_height,parent_x,parent_y):
        left = parent_x + (window_width - window_width) // 2
        top = parent_y + (window_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{left}+{top}")
        self.grab_set()  # Make the message box modal

    def create_widgets(self, message):
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text=message, wraplength=250)
        label.pack(pady=10)

        button = ctk.CTkButton(frame, text="OK", command=self.destroy)
        button.pack(pady=10)

def show_custom_message(title="Message", message="", parent_x=0, parent_y=0):
    root = ctk.CTk()
    root.withdraw()  # Hide the root window
    CustomMessageBox(root, title, message, parent_x, parent_y)
    root.mainloop()

def run_message_box(title="Info", message="", parent_x=0, parent_y=0):
    thread = threading.Thread(target=show_custom_message, args=(title, message, parent_x, parent_y))
    thread.start()

# if __name__ == "__main__":
#     run_message_box("Info", "This is a custom message box.", 900, 550)