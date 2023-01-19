import re
from pynput.keyboard import Controller
from tkinter import *
import tkinter as tk
import time
import keyboard as kb
import webbrowser
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("mac_res")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk()
#Windows Title
root.title("AutoTyper")
root.geometry("600x400")
root.resizable(0,0)
root.configure(bg = "#624F82")

#windows icon set
photo = PhotoImage(file="mac_res/icons.png")

root.iconphoto(False, photo)


keyboard = Controller()

fontSmall= ('Arial', 7)
cursor="hand2"

def callback(event):
    webbrowser.open_new_tab(event)

def rTime():
    time.sleep(5)
def rTime1():
    time.sleep(1)

def paste():
    input1=entry.get(1.0, tk.END+"-1c")
    rTime()
    keyboard.type(input1)

def paste1():
    input1=entry.get(1.0, tk.END+"-1c")
    rTime1()
    keyboard.type(input1)

def linebyline():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def singleline():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def linebyline1():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)

def singleline2():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)


canvas = Canvas(
    root,
    bg = "#a2d2ff",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    300.5,
    154.0,
    image=entry_image_1
)
entry = Text(
    bd=0,
    bg="#bde0fe",
    highlightthickness=0
)
entry.place(
    x=0.0,
    y=0.0,
    width=440.0,
    height=400.0
)

# ///////////////////
menubar = Menu(root)
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Currenty Hotkeys (shortcut keys) are not working,')
help_.add_command(label ='but dont worry we are working on that.')
help_.add_separator() 
help_.add_command(label ='                             Thank You 🌻               ')


# ////////////////////
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=singleline,
    relief="flat"
)
button_2.place(
    x=445.0,
    y=36.0,
    width=148.0,
    height=49.0
)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=linebyline,
    relief="flat"
)
button_3.place(
    x=445.0,
    y=119.0,
    width=146.0,
    height=49.0
)

canvas.create_text(
    465.0,
    343.0,
    anchor="nw",
    text="Crafted with ",
    fill="#483d8b",
    font=("Segoe Script", 8 * -2)
)

canvas.create_text(
    575.0,
    343.0,
    anchor="nw",
    text="💚",
    fill="#9370db",
    font=("Corbel", 8 * -2)
)

canvas.create_text(
    516.0,
    365.0,
    anchor="nw",
    text="by KrSatyam7",
    fill="#01796f",
    font=("Segoe Script", 11 * -1)
)



####
def openlink():
    webbrowser.open("https://github.com/krsatyam7")
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=openlink,
    relief="flat"
)
button_4.place(
    x=445.0,
    y=200.0,
    width=147.0,
    height=49.0
)
####
root.attributes('-topmost', True)
root.config(menu = menubar)

root.mainloop()
