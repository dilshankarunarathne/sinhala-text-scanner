from tkinter import messagebox
from tkinter import messagebox

from googletrans import Translator


def translate(si_text: str):
    cl = choose_language.get()
    translator = Translator()
    output = translator.translate(si_text, dest=cl)
    text_entry2.insert('end', output.text)

