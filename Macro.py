import pyautogui as bot
import time, os, sys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

value = 0
value2 = 0
image1 = '\\Img\\Riotclient.png'
image2 = '\\Img\\Username.png'
image3 = '\\Img\\LOL.png'
image4 = '\\Img\\Username2.png'
image5 = '\\Img\\RiotTop.png'
image6 = '\\Img\\logo.png'

def CallRiot():
    try:
        img1 = bot.locateCenterOnScreen(image1, confidence=0.9)

        if img1 is not None:
            bot.click(img1.x, img1.y)
            return 1
        else:
            raise ImageNotFoundException
    except ImageNotFoundException:
        os.startfile('C:\\Riot Games\\Riot Client\\RiotClientServices.exe') # <---- Put the Riot Client path in here
        return 0

def Click(number):
    time.sleep(1)
    if number == 0:
        search = 0
        while search < 60:
            try:
                img2 = bot.locateCenterOnScreen(image2, confidence=0.8)
                bot.click(img2.x, img2.y)
                search = 61
                return 1
            except:
                search += 1
        if search == 60:
            return 0

    else:
        try:
            time.sleep(1.5)
            img4 = bot.locateCenterOnScreen(image4, confidence=0.7)
            if img4 is not None:
                bot.click(img4.x, img4.y)
                return 1
            else:
                raise ImageNotFoundException
        except ImageNotFoundException:
            return 0

def typewrite(number):
    if number == 1:
        bot.write('Account',interval=0.03)
        bot.press('tab')
        bot.write('Password',interval=0.03)
        bot.press('enter')
    else:
        messagebox.showerror("Erro", "Text Box not found!")
        sys.exit()
    
def ClickOnLol():
    search = 0
    while search < 60:
        try:
            img5 = bot.locateCenterOnScreen(image5, confidence=0.8)
            img3 = bot.locateCenterOnScreen(image3, confidence=0.7)
            bot.click(img5.x, img5.y)
            time.sleep(0.4)
            bot.click(img3.x, img3.y)
            search = 61
        except:
            search += 1

    if search == 60:
        messagebox.showerror("Erro", "Image not found!")
        sys.exit()

#
#
# For now, the GUI only works with ONE account, but I will fix this later

root = tk.Tk()
root.title("My accounts - (League of Legends)")
root.geometry("450x250")
image = Image.open(image6)
image = image.resize((64, 64), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(image)
root.iconphoto(False, icon)
root.resizable(width=False, height=False)
label_name = Label(root, text='Contas:', font=('Arial 10 bold'))
label_name.place(x=0, y=10)
const = 0

def acc1():
    label_name.config(text="Entering your account")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

def acc2():
    label_name.config(text="Entering your account")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

def acc3():
    label_name.config(text="Entering your account")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

def acc4():
    label_name.config(text="Entering your account")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

button1 = tk.Button(root, text="Account 1", command=acc1, relief='groove')
button1.place(x=10, y=50)

button2 = tk.Button(root, text="Account 2", command=acc2, relief='groove')
button2.place(x=10, y=90)

button3 = tk.Button(root, text="Account 3", command=acc3, relief='groove')
button3.place(x=10, y=130)

button4 = tk.Button(root, text="Account 4", command=acc4, relief='groove')
button4.place(x=10, y=170)

root.mainloop()
