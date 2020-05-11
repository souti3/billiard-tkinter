#!/usr/bin/python3

import tkinter
from tkinter import messagebox
top = tkinter.Tk()
top.title("Hello stranger")



# Code to add widgets will go here...

frame1 = tkinter.Frame(top)
frame1.pack(padx=10, pady=10)

bgtext = tkinter.StringVar()
label = tkinter.Label( frame1, textvariable=bgtext )
bgtext.set("""Guten Tag! \n Dies ist ein Hello World Programm! 
Für eine persönliche Begrüssung, geben Sie Ihren Namen in das Textfeld ein und klicken anschliessend auf den Knopf.\n""")
label.pack(padx=10, pady=10)

frame2 = tkinter.Frame(top)
frame2.pack()

nameLabel = tkinter.Label(frame2, text = "Ihr Name:")
nameLabel.pack( side = tkinter.LEFT, padx=10, pady=10)
nameEntry = tkinter.Entry(frame2, bd = 5)
nameEntry.pack(side = tkinter.RIGHT, padx=10, pady=10)

frame3 = tkinter.Frame(top)
frame3.pack()

def helloCallBack():
    name = nameEntry.get()
    greetings = "Hello " + name + "!"
    msg = messagebox.showinfo( "Hello", greetings)

###
def toggle_state(*_):
    if nameEntry.var.get():
        hello['state'] = 'normal'
    else:
        hello['state'] = 'disabled'

nameEntry.var = tkinter.StringVar()
nameEntry['textvariable'] = nameEntry.var
nameEntry.var.trace_add('write', toggle_state)

hello = tkinter.Button ( frame3, text="Begrüssung", command=helloCallBack, state=tkinter.DISABLED )


hello.pack(side=tkinter.BOTTOM , padx=10, pady=10)

top.mainloop()