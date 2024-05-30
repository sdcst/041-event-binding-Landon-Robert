#!python 3
# same program, better use of variables!
import tkinter as tk
import playsound as p
from playsound import *
def playsound1():
    playsound("plants-vs-zombies-victory-jingle.mp3")
def playsound2():
    playsound("vine-boom.mp3")
def playsound3():
    playsound("gun-load.mp3")
def playsound4():
    playsound("plants-vs-zombies-victory-jingle.mp3")
def playsound5():
    playsound("plants-vs-zombies-victory-jingle.mp3")


window = tk.Tk()
window.geometry("200x300")
l1 = tk.Label(window,text="PVZ Victory riff")
l2 = tk.Label(window,text="Vine Boom")
l3 = tk.Label(window,text="Gun Load")
b1 = tk.Button(window,text="Click to play",command=playsound1)
b2 = tk.Button(window,text="Click to play",command=playsound2)
b3 = tk.Button(window,text="Click to play",command=playsound3)
b4 = tk.Button(window,text="Click to play",command=playsound4)
b5 = tk.Button(window,text="Click to play",command=playsound5)

l1.pack()
b1.pack()
l2.pack()
b2.pack()
l3.pack()
b3.pack()


window.mainloop()