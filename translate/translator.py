from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox



def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter to the translate')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)


auto_select = ttk.Combobox(frame1, width=27, textvariable=a, state='randomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
    'Auto Select',
)
auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='randomly', font=('vendana', 10, 'bold'))

choose_language['values'] = (
    'English',
    'Sinhala',
    'Tamil',
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Bengali',
    'Chinese',
    'Corsican',
    'Danish',
    'Greek',
    'Gujarati',
    'Hindi',
    'Japanese',
    'Korean',
    'Latin',
    'Malagasy',
    'Mongolian',
    'Punjabi',
    'Romanian',
    'russian',
    'Telugu',
    'Zulu'
)

choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(frame1, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(frame1, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn2.place(x=300, y=300)

root.mainloop()
