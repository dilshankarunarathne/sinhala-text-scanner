from tkinter import messagebox
from tkinter import messagebox

from googletrans import Translator

translator = Translator()

def translate(si_text: str):
    output = translator.translate(si_text, dest=cl)
    text_entry2.insert('end', output.text)

