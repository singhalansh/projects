import pygame
from tkinter import * #type: ignore

import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
pygame.init()
music = pygame.mixer.music

file = None
def open():
    global file
    file =askopenfilename()
    music.load(file)
    name = os.path.basename(file)
    text.set(name)
def play():
    music.play()
def pause():
    music.pause()
def resume():
    music.unpause()
def vol_up():
    current_vol = music.get_volume()
    new_vol = current_vol +0.1
    music.set_volume(new_vol)
def vol_down():
    current_vol = music.get_volume()
    new_vol = current_vol -0.1
    music.set_volume(new_vol)

win = Tk()
text = StringVar()
win.resizable(False,False)
win.geometry("400x400+450+100")
win.title("MUSIC PLAYER BY ANSH")
win.configure(bg="green")
f1 = Frame(win)
Entry(f1,textvariable=text,font="comicsansms 24").pack(side=TOP,fill="x")
f1.pack(fill="x")
f2 = Frame(win,bg="green")
open_button = Button(f2,text="Open",width=15,height=3,bg="skyblue",font="arialblack 15 bold",command=open)
open_button.pack()
play_button = Button(f2,text="Play",command=play,width=15,height=3,bg="skyblue",font="arialblack 15 bold").pack(pady=20)
pause_button = Button(f2,text="Pause",width=15,command=pause,height=3,bg="skyblue",font="arialblack 15 bold").pack()

f2.pack(side=LEFT)
f3 = Frame(win,bg="green")
resume_button = Button(f3,command=resume,text="Resume",width=15,height=3,bg="skyblue",font="arialblack 15 bold").pack()
vol_up_button = Button(f3,text="VOL UP",width=15,height=3,bg="skyblue",font="arialblack 15 bold",command=vol_up).pack(pady=20)
vol_down_button = Button(f3,text="VOL DOWN",width=15,height=3,bg="skyblue",font="arialblack 15 bold",command=vol_down).pack()

f3.pack(side=RIGHT)

win.mainloop()
