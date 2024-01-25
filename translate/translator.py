from tkinter import messagebox
from tkinter import messagebox

from googletrans import Translator

translator = Translator()

def translate(si_text: str):
    return translator.translate(si_text, dest=cl)
