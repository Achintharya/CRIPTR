import hashlib
import json
from tkinter import BOTH
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkTextbox, CTkButton, CTkFont
from deep_translator import GoogleTranslator
from spellchecker import SpellChecker
import asyncio
from CustomMessagebox import show_custom_message

class EnCrypt(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EnCryption")
        self.hash_values = self.load_hash_values()  # Load hash values at start
        self.setup_window()
        self.create_menu()
        self.mainloop()

    def setup_window(self):
        window_width = 900
        window_height = 550
        left = (self.winfo_screenwidth() - window_width) // 2
        top = (self.winfo_screenheight() - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{left}+{top}")
        self.bind("<Escape>", lambda event: self.quit())

    def create_menu(self):
        menu = Menu(self)
        menu.pack(expand=True, fill=BOTH)

    def load_hash_values(self):
        try:
            with open("hash_values.json", "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}

class Menu(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent  # Reference to the parent EnCrypt class
        self.create_widgets_layout()
        self.spell_checker = SpellChecker()
        self.translation_cache = {}

    def create_widgets_layout(self):
        top_frame = CTkFrame(self, fg_color="transparent")
        mid_frame = CTkFrame(self, fg_color="transparent")
        bottom_frame = CTkFrame(self, fg_color="transparent")
        
        font = CTkFont(family="<Arial>", size=20, weight="bold")

        data_label = CTkLabel(top_frame, text="Enter data to Encrypt : ", font=font)
        self.data_entry = CTkTextbox(top_frame, height=200, width=400, font=font)
        encode_button = CTkButton(top_frame, text="Encode", command=self.encode, hover_color="green")
        result_label_name = CTkLabel(mid_frame, text="Encoded data : ", font=font, anchor="e")
        self.result_label = CTkLabel(mid_frame, text="Wait for it", font=CTkFont(family="<Arial>", size=12, slant="italic"), wraplength=350, justify="left")
        exit_button = CTkButton(bottom_frame, text="Exit", command=self.exit, hover_color="red", font=CTkFont(size=23))
        copy_button = CTkButton(bottom_frame, text="Copy Encrypted text", command=self.copy, hover_color="dark blue", font=CTkFont(size=23))
        
        top_frame.pack(side="top", pady=10)
        mid_frame.pack(side="top", pady=20)
        bottom_frame.pack(side="bottom")

        data_label.pack(side="left")
        self.data_entry.pack(padx=10)
        encode_button.pack(padx=10)
        result_label_name.pack(side="left", pady=10)
        self.result_label.pack(side="left", pady=10)
        exit_button.grid(row=0, column=0, padx=(0, 250), pady=10, sticky="e")
        copy_button.grid(row=0, column=1, padx=(250, 0), pady=10, sticky="w")

    def exit(self):
        self.master.destroy()

    async def encode_async(self):
        data = self.data_entry.get("1.0", "end-1c").strip()
        encoded_data = ""
        hash_values = self.parent.hash_values  # Reference the parent's hash values

        words = data.split()
        batch_size = 5
        for i in range(0, len(words), batch_size):
            batch = words[i:i+batch_size]

            # Preprocess and spell check the batch
            preprocessed_batch = [self.spell_checker.correction(word) for word in batch]

            # Translate the batch asynchronously
            translations = await self.translate_batch(preprocessed_batch)

            for word, translation_es, translation_hi in translations:
                partial_spanish = translation_es[:2] if translation_es is not None else word[:2]
                partial_hindi = translation_hi[-2:] if translation_hi is not None else word[-2:]
                
                if word in hash_values:
                    hash_value = hash_values[word]
                else:
                    hash_value = int(hashlib.sha256(word.encode()).hexdigest(), 16) % 899 + 100
                    hash_values[word] = hash_value  # Update hash values dictionary
                    
                encoded_data += f"{partial_spanish}Ω{hash_value}Ω{partial_hindi} "

        # Save the updated hash values to file
        with open("hash_values.json", "w") as json_file:
            json.dump(hash_values, json_file)

        self.result_label.configure(text=encoded_data.strip())

        with open("ENCRYPTED_TEXT.txt", "w", encoding="utf-8") as f:
            f.write(encoded_data.strip())

    async def translate_batch(self, batch):
        translations = []
        for word in batch:
            if word in self.translation_cache:
                translations.append(self.translation_cache[word])
            else:
                translation_es = await asyncio.to_thread(GoogleTranslator(source='en', target='es').translate, word)
                translation_hi = await asyncio.to_thread(GoogleTranslator(source='auto', target='hi').translate, word)
                translations.append((word, translation_es, translation_hi))
                self.translation_cache[word] = (word, translation_es, translation_hi)
        
        return translations

    def encode(self):
        asyncio.run(self.encode_async())

    def copy(self):
        text_to_copy = self.result_label.cget("text")
        self.clipboard_clear()
        self.clipboard_append(text_to_copy)
        show_custom_message(title="Info", message="Copied text to clipboard",parent_x=900,parent_y=550)