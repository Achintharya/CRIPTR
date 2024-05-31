import tkinter as Tk
from tkinter import *
import json

def DeCrypt():
    top2 = Tk()
    top2.title("DeCryption")
    top2.geometry("700x450")
    top2.configure(bg="light blue")

    def exit2():
        return top2.destroy()

    def decode():
        encoded_data = str(data2_entry.get())
        decoded_data = ""

        # Read hash values from the JSON file
        with open("HASH_VALUES.json", "r") as json_file:
            hash_values = json.load(json_file)

        for encoded_word in encoded_data.split(" "):
            components = encoded_word.strip().split("§")
            hash_value_str = components[1]  # Extract hash value from components

            # Use hash value to find the original word
            for word, hash_value in hash_values.items():
                if str(hash_value) == hash_value_str:
                    decoded_data += word + " "
                    break
            else:
                decoded_data += "ERROR: Failed to decode word\n"

        result_label.config(text=decoded_data.strip())

    data2 = Label(
        top2, text="Enter data to Decrypt : ", font="Arial 16 bold", bg="light blue"
    ).grid(row=1, column=0)

    data2_entry = Entry(top2)
    data2_entry.grid(row=1, column=1)

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

    exit2_button = Button(
        top2,
        text="Exit",
        command=exit2,
        bg="red",
        fg="white",
        activebackground="magenta",
        font=23,
    ).grid(row=5, column=2)

