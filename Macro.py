import pyautogui as bot
import time, os, sys
import tkinter as tk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

value = 0
value2 = 0
image1 = 'Img\\Riotclient.png'    ## <-- YOU HAVE TO PUT THE PATH OF THE IMAGE HERE
image2 = 'Img\\Username.png'    ## <-- YOU HAVE TO PUT THE PATH OF THE IMAGE HERE
image3 = 'Img\\LOL.png'    ## <-- YOU HAVE TO PUT THE PATH OF THE IMAGE HERE
image4 = 'Img\\Username2.png'    ## <-- YOU HAVE TO PUT THE PATH OF THE IMAGE HERE

def window():
    root = tk.Tk()
    root.title("Contas LOL")
    ## GUI(in development)

def CallRiot():
    try:
        img1 = bot.locateCenterOnScreen(image1, confidence=0.9)

        if img1 is not None:
            bot.click(img1.x, img1.y)
            return 1
        else:
            raise ImageNotFoundException
    except ImageNotFoundException:
        os.startfile('RiotClientServices.exe') ## <-- YOU HAVE TO PUT THE PATH OF THE RIOT CLIENT HERE
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

def typewrite(number):    ##Account
    if number == 1:
        bot.write('account',interval=0.03) ## <-- Your Username
        bot.press('tab')
        bot.write('password',interval=0.03) ## <-- Your Password
        bot.press('enter')
    else:
        messagebox.showerror("Error", "Box not found!")
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
        messagebox.showerror("Error", "Box not found!")
        sys.exit()


value2 = CallRiot()
value = Click(value2)
typewrite(value)
ClickOnLol()
