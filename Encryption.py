import tkinter as Tk
from tkinter import *
import hashlib
from deep_translator import GoogleTranslator
import json

def EnCrypt():
    top1 = Tk()
    top1.configure(bg="Light blue")
    top1.geometry("460x300")
    top1.title("EnCryption")

    def exit1():
        return top1.destroy()

    def encode():
        data = str(data1_entry.get())
        encoded_data = ""
        hash_values = {}

        for word in data.split():
            # Translate the English word to Spanish partially
            partial_spanish = GoogleTranslator(source='en', target='es').translate(word)[:3]

            # Generate a unique consistent number using hashlib for the word
            hash_value = int(hashlib.sha256(word.encode()).hexdigest(), 16) % 899 + 100
            hash_values[word] = hash_value  # Store hash value for the word

            # Translate the word to Hindi partially
            partial_hindi = GoogleTranslator(source='auto', target='hi').translate(word)[-3:]

            encoded_data += partial_spanish + "§" + str(hash_value) + "§" + partial_hindi + " "

        # Write hash values to a JSON file
        with open("hash_values.json", "w") as json_file:
            json.dump(hash_values, json_file)

        result_label.config(text=encoded_data.strip())

        # Open the file with UTF-8 encoding
        with open("ENCRYPTED_DATA.txt", "w", encoding="utf-8") as f:
            f.write(encoded_data.strip())

    def copy():
        return top1.clipboard_append((result_label["text"]))

    data1 = Label(
        top1, text="Enter data to Encrypt : ", font="Arial 16 bold", bg="light blue"
    ).grid(row=0, column=0)
    data1_entry = Entry(top1)
    data1_grid = data1_entry.grid(row=0, column=1)
    data1_button = Button(
        top1,
        text="Encode",
        command=encode,
        bg="pink",
        fg="navy blue",
        activebackground="green",
    ).grid(row=0, column=2)

    result_name = Label(
        top1, text="EnCrypted data : ", font="Arial 16 bold", bg="light blue"
    ).grid(row=2, column=0)
    result_label = Label(top1, bg="Light blue", font=10)
    result_label.grid(row=2, column=1)

    blah1 = Label(top1, bg="light blue").grid(row=4, column=2)
    exit1_button = Button(
        top1,
        text="Exit",
        command=exit1,
        bg="red",
        fg="white",
        activebackground="magenta",
        font=23,
    ).grid(row=5, column=2)

    blah2 = Label(top1, bg="light blue").grid(row=6, column=2)

    copy_b = Button(
        top1,
        text="Copy Encrypted text",
        command=copy,
        bg="blue",
        fg="white",
        activebackground="purple",
        font=23,
    ).grid(row=5, column=0)

