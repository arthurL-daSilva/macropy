import pyautogui as bot
import time, os, sys
import threading
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

image1 = '\\Img\\Riotclient.png'
image2 = '\\Img\\Username.png'
image3 = '\\Img\\LOL.png'
image4 = '\\Img\\Username2.png'
image5 = '\\Img\\RiotTop.png'
image6 = '\\Img\\logo.png'
image7 = '\\Img\\League_open.png'
data_file = 'account_data.txt'
data_path = 'Riot_Client_path.txt'

def CallRiot():
    try:
        img1 = bot.locateCenterOnScreen(image1, confidence=0.9)
        if img1 is not None:
            bot.click(img1.x, img1.y)
            return 1
        else:
            raise ImageNotFoundException
    except ImageNotFoundException:
        os.startfile(application_path.get())
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

def typewrite_account(username, password, number):
    if number == 1:
        bot.write(username, interval=0.02)
        bot.press('tab')
        bot.write(password, interval=0.02)
        bot.press('enter')
    else:
        messagebox.showerror("Error", "Text box not found!")
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
        messagebox.showerror("Error", "Image not found!")
        sys.exit()

def load_account_data():
    if not os.path.exists(data_file):
        messagebox.showwarning("Warning", "Data file not found. Add any account to create-it.")
        return

    with open(data_file, 'r') as file:
        lines = file.readlines()

        if len(lines) >= 1:
            entry_user1.insert(0, lines[0].strip())
        if len(lines) >= 2:
            entry_pass1.insert(0, lines[1].strip())
        if len(lines) >= 3:
            entry_user2.insert(0, lines[2].strip())
        if len(lines) >= 4:
            entry_pass2.insert(0, lines[3].strip())
        if len(lines) >= 5:
            entry_user3.insert(0, lines[4].strip())
        if len(lines) >= 6:
            entry_pass3.insert(0, lines[5].strip())
        if len(lines) >= 7:
            entry_user4.insert(0, lines[6].strip())
        if len(lines) >= 8:
            entry_pass4.insert(0, lines[7].strip()) 

def save_account_data():
    with open(data_file, 'w') as file:
        file.write(entry_user1.get() + '\n')
        file.write(entry_pass1.get() + '\n')
        file.write(entry_user2.get() + '\n')
        file.write(entry_pass2.get() + '\n')
        file.write(entry_user3.get() + '\n')
        file.write(entry_pass3.get() + '\n')
        file.write(entry_user4.get() + '\n')
        file.write(entry_pass4.get() + '\n')

def League_Open():
    try:
        img7 = bot.locateCenterOnScreen(image7, confidence=0.7)
        if img7 is not None:
            messagebox.showwarning('Warning','Your game is already open!')
            return 0
        else:
            raise ImageNotFoundException
    except ImageNotFoundException:
        return 1

root = tk.Tk()
root.title("My accounts - (League of Legends)")
root.geometry("650x370")
image = Image.open(image6)
image = image.resize((64, 64), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(image)
root.iconphoto(False, icon)
application_path = StringVar()
label_name = Label(root, text='Accounts:', font=('Arial 10 bold'))
label_name.place(x=10, y=10)

label_footer_main = Label(root, text='---------------------------------------------------------------------------------------------------------------------------------------------------------------', font='Arial 10')
label_footer_main.place(x=5, y=30)

label_user1 = Label(root, text="Account 1:")
label_user1.place(x=10, y=60)
entry_user1 = Entry(root)
entry_user1.place(x=100, y=60)

label_pass1 = Label(root, text="Password:")
label_pass1.place(x=10, y=85)
entry_pass1 = Entry(root, show='*')
entry_pass1.place(x=100, y=85)

label_user2 = Label(root, text="Account 2:")
label_user2.place(x=10, y=140)
entry_user2 = Entry(root)
entry_user2.place(x=100, y=140)

label_pass2 = Label(root, text="Password:")
label_pass2.place(x=10, y=165)
entry_pass2 = Entry(root, show='*')
entry_pass2.place(x=100, y=165)

label_user3 = Label(root, text="Account 3:")
label_user3.place(x=10, y=220)
entry_user3 = Entry(root)
entry_user3.place(x=100, y=220)

label_pass3 = Label(root, text="Password:")
label_pass3.place(x=10, y=245)
entry_pass3 = Entry(root, show='*')
entry_pass3.place(x=100, y=245)

label_user4 = Label(root, text="Account 4:")
label_user4.place(x=10, y=300)
entry_user4 = Entry(root)
entry_user4.place(x=100, y=300)

label_pass4 = Label(root, text="Password:")
label_pass4.place(x=10, y=325)
entry_pass4 = Entry(root, show='*')
entry_pass4.place(x=100, y=325)

label_path = Label(root, text="Riot Client not selected.", font='Arial 8 bold')
label_path.place(x=480, y=13)

def execute_account(username, password):
    
    with open(data_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 1:
            value3 = League_Open()
            if value3 == 1:
                value2 = CallRiot()
                value = Click(value2)
                typewrite_account(username, password, value)
                save_account_data()
                ClickOnLol()
        else:
            messagebox.showerror('Select the Riot Client.', 'Riot Client not selected')

def select_RiotClient():
    file_path = filedialog.askopenfilename(title="Select the Riot Client", filetypes=[("executables", "*.exe")])
    if file_path:
        application_path.set(file_path)
        label_path.config(text="Riot Client ready!")
        with open(data_path, 'w') as file:
            file.write(file_path)

def load_RiotClient_path():
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            file_path = file.read().strip()
            if file_path:
                application_path.set(file_path)
                label_path.config(text="Riot Client ready!")


def acc1():
    if not entry_user1.get() or not entry_pass1.get():
        messagebox.showwarning("Warning", "User or password of the account 1 is not registered.")
        return

    label_name.config(text="Entrando na "+ entry_user1.get())
    threading.Thread(target=execute_account, args=(entry_user1.get(), entry_pass1.get())).start()

def acc2():
    if not entry_user2.get() or not entry_pass2.get():
        messagebox.showwarning("Warning", "User or password of the account 2 is not registered.")
        return

    label_name.config(text="Entrando na "+ entry_user2.get())
    threading.Thread(target=execute_account, args=(entry_user2.get(), entry_pass2.get())).start()

def acc3():
    if not entry_user3.get() or not entry_pass3.get():
        messagebox.showwarning("Warning", "User or password of the account 3 is not registered.")
        return

    label_name.config(text="Entrando na "+ entry_user3.get())
    threading.Thread(target=execute_account, args=(entry_user3.get(), entry_pass3.get())).start()

def acc4():
    if not entry_user4.get() or not entry_pass4.get():
        messagebox.showwarning("Warning", "User or password of the account 4 is not registered.")
        return

    label_name.config(text="Entrando na "+ entry_user4.get())
    threading.Thread(target=execute_account, args=(entry_user4.get(), entry_pass4.get())).start()

button1 = tk.Button(root, text="Enter in acc 1", command=acc1, relief='groove')
button1.place(x=300, y=70)

button2 = tk.Button(root, text="Enter in acc 2", command=acc2, relief='groove')
button2.place(x=300, y=152)

button3 = tk.Button(root, text="Enter in acc 3", command=acc3, relief='groove')
button3.place(x=300, y=232)

button4 = tk.Button(root, text="Enter in acc 4", command=acc4, relief='groove')
button4.place(x=300, y=312)

button_path = tk.Button(root, text="Select RiotClient", command=select_RiotClient, relief='groove')
button_path.place(x=475, y=70)

load_account_data()
load_RiotClient_path()

root.mainloop()