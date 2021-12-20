from tkinter import *
from tkinter import font
import pyttsx3

window = Tk()
window.title('Text-to-Speech App by Souvik Roy')
window.config(bg="#fff")
window.iconbitmap('icon.ico')


def say():
    engine = pyttsx3.init()
    text = entry.get(1.0, END)
    engine.say(text)
    engine.runAndWait()


title = Label(window, text="Text-to-Speech App by Souvik Roy", font=('MV Boli', 20), fg="blue", bg="#fff")
title.pack()

enter = Button(window, text="Click here", font=('BahnSchript', 24), fg="blue", bg="#f7f7f7", bd=0, command=lambda: say())
enter.pack(fill=X, side=BOTTOM)

verticalscrollbar = Scrollbar()
verticalscrollbar.pack(fill=Y, side=RIGHT)

entry = Text(window, font=('Calibri', 12), yscrollcommand=verticalscrollbar.set)
entry.pack(fill=X)

verticalscrollbar.config(command=entry.yview)

window.mainloop()
