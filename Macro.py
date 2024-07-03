import pyautogui as bot
import time, os, sys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

value = 0
value2 = 0
image1 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Riotclient.png'
image2 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Username.png'
image3 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\LOL.png'
image4 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Username2.png'
image5 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\RiotTop.png'
image6 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\logo.png'

def CallRiot():
    try:
        img1 = bot.locateCenterOnScreen(image1, confidence=0.9)

        if img1 is not None:
            bot.click(img1.x, img1.y)
            return 1
        else:
            raise ImageNotFoundException
    except ImageNotFoundException:
        os.startfile('C:\\Riot Games\\Riot Client\\RiotClientServices.exe')
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
        bot.write('jesterdeath3',interval=0.03)
        bot.press('tab')
        bot.write('casa470a',interval=0.03)
        bot.press('enter')
    else:
        messagebox.showerror("Erro", "Caixa de texto não encontrada!")
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
        messagebox.showerror("Erro", "Imagem não encontrada!")
        sys.exit()

root = tk.Tk()
root.title("Minhas contas - (League of Legends)")
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
    label_name.config(text="Entrando na Main")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

def acc2():
    label_name.config(text="Entrando na Death")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

def acc3():
    label_name.config(text="Entrando na Valleyy2")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

def acc4():
    label_name.config(text="Entrando na Sekiryyuutei")
    value2 = CallRiot()
    value = Click(value2)
    typewrite(value)
    ClickOnLol()

button1 = tk.Button(root, text="jester2146", command=acc1, relief='groove')
button1.place(x=10, y=50)

button2 = tk.Button(root, text="jester death", command=acc2, relief='groove')
button2.place(x=10, y=90)

button3 = tk.Button(root, text="Valleyy2", command=acc3, relief='groove')
button3.place(x=10, y=130)

button4 = tk.Button(root, text="Sekiryyuutei", command=acc4, relief='groove')
button4.place(x=10, y=170)

root.mainloop()