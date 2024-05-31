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
    playsound("taco-bell-bong-sfx.mp3")
def playsound5():
    playsound("enter-painting.mp3")
def playsound6():
    playsound("among-us-start.mp3")


window = tk.Tk()
window.geometry("280x120")
l1 = tk.Label(window,text="PVZ Victory riff")
l2 = tk.Label(window,text="Vine Boom")
l3 = tk.Label(window,text="Gun Load")
l4 = tk.Label(window,text="Taco Bell")
l5 = tk.Label(window,text="Mario 64 painting")
l6 = tk.Label(window,text="Among us start")
b1 = tk.Button(window,text="Click to play",command=playsound1)
b2 = tk.Button(window,text="Click to play",command=playsound2)
b3 = tk.Button(window,text="Click to play",command=playsound3)
b4 = tk.Button(window,text="Click to play",command=playsound4)
b5 = tk.Button(window,text="Click to play",command=playsound5)
b6 = tk.Button(window,text="Click to play",command=playsound6)

l1.grid(row=1,column=1)
b1.grid(row=2,column=1)
l2.grid(row=1,column=2)
b2.grid(row=2,column=2)
l3.grid(row=1,column=3)
b3.grid(row=2,column=3)
l4.grid(row=3,column=1)
b4.grid(row=4,column=1)
l5.grid(row=3,column=2)
b5.grid(row=4,column=2)
l6.grid(row=3,column=3)
b6.grid(row=4,column=3)

window.mainloop()