from tkinter import *
from random import randrange as rnd, choice
import tkinter as tk
import math
import time

def lets_play():
    root = Tk()
    root.title("Anal Piano")
    root.geometry("1366x768")
    
    C = Canvas(root, bg="blue", height=1366, width=768)
    filename = PhotoImage(file = "white1.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.resizable(width=False, height=False)
    
    C.pack()

    btn = Button(text="PIANO PIANO", background="grey", foreground="white", activebackground="grey",
                  activeforeground="white",
                  padx="20", pady="8", font="50")
    btn.place(relx=.2, rely=.2, anchor="c", height=60, width=200, bordermode=OUTSIDE)    

    btn1 = Button(text="start game", background="grey", foreground="white", activebackground="red",
                  activeforeground="green",
                  padx="20", pady="8", font="16")
    btn1.place(relx=.48, rely=.44, anchor="c", height=60, width=200, bordermode=OUTSIDE)

    btn2 = Button(text="music", background="grey", foreground="white", activebackground="red",
                  activeforeground="green",
                  padx="20", pady="8", font="16")
    btn2.place(relx=.48, rely=.75, anchor="c", height=60, width=130, bordermode=OUTSIDE)
    
    
    
    l1 = Label(text="asa", font="Arial 32")
    l2 = Label(text="sasas", font=("Comic Sans MS", 24, "bold"))
    l1.config(bd=20, bg='#ffaaaa')
    l2.config(bd=20, bg='#aaffff')
    l1.pack()
    l2.pack()
    
    root.mainloop()
lets_play()