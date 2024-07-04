import pyautogui as bot
import time, os, sys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

image1 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Riotclient.png'
image2 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Username.png'
image3 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\LOL.png'
image4 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Username2.png'
image5 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\RiotTop.png'
image6 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\logo.png'
data_file = 'account_data.txt'

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

def typewrite_account(username, password, number):
    if number == 1:
        bot.write(username, interval=0.03)
        bot.press('tab')
        bot.write(password, interval=0.03)
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

def load_account_data():
    if not os.path.exists(data_file):
        messagebox.showwarning("Aviso", "Arquivo de dados não encontrado. Adicione alguma conta para cria-lo.")
        return

    with open(data_file, 'r') as file:
        lines = file.readlines()
        if len(lines) < 1:
            messagebox.showwarning("Aviso", "Nenhuma conta encontrada.")
            return

        if len(lines) >= 1:
            entry_user1.insert(0, lines[0].strip()) #0  -> começando na posição 0
        if len(lines) >= 2:
            entry_pass1.insert(0, lines[1].strip()) #lines[1] -> seria o número da linha contida no arquivo
        if len(lines) >= 3:
            entry_user2.insert(0, lines[2].strip()) #.strip() -> Remove espaços em branco
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
        file.write(entry_user1.get() + '\n') #entry_user.get() -> escreve o conteúdo do campo de entrada no arquivo, seguido por um caracter de nova linha '\n'
        file.write(entry_pass1.get() + '\n')
        file.write(entry_user2.get() + '\n')
        file.write(entry_pass2.get() + '\n')
        file.write(entry_user3.get() + '\n')
        file.write(entry_pass3.get() + '\n')
        file.write(entry_user4.get() + '\n')
        file.write(entry_pass4.get() + '\n') 

root = tk.Tk()
root.title("Minhas contas - (League of Legends)")
root.geometry("450x300")
image = Image.open(image6)
image = image.resize((64, 64), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(image)
root.iconphoto(False, icon)
root.resizable(width=False, height=False)
label_name = Label(root, text='Contas:', font=('Arial 10 bold'))
label_name.place(x=10, y=10)

label_user1 = Label(root, text="Conta 1:")
label_user1.place(x=10, y=50)
entry_user1 = Entry(root)
entry_user1.place(x=100, y=50)

label_pass1 = Label(root, text="Senha 1:")
label_pass1.place(x=10, y=80)
entry_pass1 = Entry(root, show='*')
entry_pass1.place(x=100, y=80)

label_user2 = Label(root, text="Conta 2:")
label_user2.place(x=10, y=110)
entry_user2 = Entry(root)
entry_user2.place(x=100, y=110)

label_pass2 = Label(root, text="Senha 2:")
label_pass2.place(x=10, y=140)
entry_pass2 = Entry(root, show='*')
entry_pass2.place(x=100, y=140)

label_user3 = Label(root, text="Conta 3:")
label_user3.place(x=10, y=170)
entry_user3 = Entry(root)
entry_user3.place(x=100, y=170)

label_pass3 = Label(root, text="Senha 3:")
label_pass3.place(x=10, y=200)
entry_pass3 = Entry(root, show='*')
entry_pass3.place(x=100, y=200)

label_user4 = Label(root, text="Conta 4:")
label_user4.place(x=10, y=230)
entry_user4 = Entry(root)
entry_user4.place(x=100, y=230)

label_pass4 = Label(root, text="Senha 4:")
label_pass4.place(x=10, y=260)
entry_pass4 = Entry(root, show='*')
entry_pass4.place(x=100, y=260)

def acc1():
    if not entry_user1.get() or not entry_pass1.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 1 não está registrado.")
        return

    label_name.config(text="Entrando na Conta 1")
    value2 = CallRiot()
    value = Click(value2)
    username = entry_user1.get()
    password = entry_pass1.get()
    typewrite_account(username, password, value)
    save_account_data()
    ClickOnLol()

def acc2():
    if not entry_user2.get() or not entry_pass2.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 2 não está registrado.")
        return

    label_name.config(text="Entrando na Conta 2")
    value2 = CallRiot()
    value = Click(value2)
    username = entry_user2.get()
    password = entry_pass2.get()
    typewrite_account(username, password, value)
    save_account_data()
    ClickOnLol()

def acc3():
    if not entry_user3.get() or not entry_pass3.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 3 não está registrado.")
        return

    label_name.config(text="Entrando na Conta 3")
    value2 = CallRiot()
    value = Click(value2)
    username = entry_user3.get()
    password = entry_pass3.get()
    typewrite_account(username, password, value)
    save_account_data()
    ClickOnLol()

def acc4():
    if not entry_user4.get() or not entry_pass4.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 4 não está registrado.")
        return

    label_name.config(text="Entrando na Conta 4")
    value2 = CallRiot()
    value = Click(value2)
    username = entry_user4.get()
    password = entry_pass4.get()
    typewrite_account(username, password, value)
    save_account_data()
    ClickOnLol()

button1 = tk.Button(root, text="Entrar na Conta 1", command=acc1, relief='groove')
button1.place(x=300, y=50)

button2 = tk.Button(root, text="Entrar na Conta 2", command=acc2, relief='groove')
button2.place(x=300, y=110)

button3 = tk.Button(root, text="Entrar na Conta 3", command=acc3, relief='groove')
button3.place(x=300, y=170)

button4 = tk.Button(root, text="Entrar na Conta 4", command=acc4, relief='groove')
button4.place(x=300, y=230)

load_account_data()

root.mainloop()
