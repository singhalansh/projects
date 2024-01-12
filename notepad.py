from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))


def info():
    tmsg.showinfo("about me", "this notepad is made by akhilesh")


def new():
    
    a = tmsg.askyesnocancel("save", "would you like to save it")
    if a == YES:
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All files",
                                                                                                      "*.*"), (
                                                                                                     "Text Documents",
                                                                                                     "*.txt")])
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(text.get(1.0, END))
                f.close()
                root.title(os.path.basename(file))
    elif a == NO:
        root.title("Untitled - Notepad")
        file = None
        text.delete(1.0, END)
    else:
        file = None


def o():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files",
                                                                "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file))
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All files",
                                                                                                  "*.*"), (
                                                                                                 "Text Documents",
                                                                                                 "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            root.title(os.path.basename(file))
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()
        root.title(os.path.basename(file))


root.iconbitmap(None)

root.title("Untitled - Notepad")

root.geometry("500x500")

file = None

# menus starts

mainmenu = Menu(root)

# file menu starts

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=o)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Exit", command=root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)

# file menu ends

# edit menu starts

Editmenu = Menu(mainmenu, tearoff=0)
Editmenu.add_command(label="Undo", command=new)
Editmenu.add_command(label="cut", command=cut)
Editmenu.add_command(label="copy", command=copy)
Editmenu.add_command(label="paste", command=paste)

mainmenu.add_cascade(label="Edit", menu=Editmenu)

# edit menu ends

infomenu = Menu(mainmenu, tearoff=0)
infomenu.add_command(label="developer Info", command=info)

mainmenu.add_cascade(label="Info", menu=infomenu)

root.config(menu=mainmenu)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root, font="arialblack 18", yscrollcommand=scrollbar.set)
text.pack(fill=BOTH, expand=True)
scrollbar.config(command=text.yview)

root.mainloop()