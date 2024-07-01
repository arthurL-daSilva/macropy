import pyautogui as bot
import time, os, sys
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

value = 0
value2 = 0
image1 = 'E:\\PROJETOS\\Programming Languages\\Python\\Img\\Riotclient.png'
image2 = 'E:\\PROJETOS\\Programming Languages\\Python\\Img\\Username.png'
image3 = 'E:\\PROJETOS\\Programming Languages\\Python\\Img\\LOL.png'
image4 = 'E:\\PROJETOS\\Programming Languages\\Python\\Img\\Username2.png'

def window():
    root = tk.Tk()
    root.title("Minhas contas - (League of Legends)")
    root.geometry("450x250")
    root.config(background="#4F4F4F")
    icon_path = 'Img\\logo.png'
    image = Image.open(icon_path)
    image = image.resize((64, 64), Image.Resampling.LANCZOS)
    icon = ImageTk.PhotoImage(image)
    root.iconphoto(False, icon)
    root.resizable(width=False, height=False)
    root.mainloop()
    ##For now, it does nothing

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
    if number == 0:
        try:
            time.sleep(8)
            img2 = bot.locateCenterOnScreen(image2, confidence=0.8)
            if img2 is not None:
                bot.click(img2.x, img2.y)
                return 1
            else:
                raise ImageNotFoundException
        except ImageNotFoundException:
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
            img3 = bot.locateCenterOnScreen(image3, confidence=0.7)
            bot.click(img3.x, img3.y)
            search = 61
        except:
            search += 1

    if search == 60:
        messagebox.showerror("Error", "Imagem não encontrada!")
        sys.exit()

window()
value2 = CallRiot()
value = Click(value2)
typewrite(value)
ClickOnLol()
