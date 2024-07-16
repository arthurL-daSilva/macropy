import pyautogui as bot
import time, os, sys
import threading
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from pyautogui import ImageNotFoundException

image1 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Riotclient.png'
image2 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Username.png'
image3 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\LOL.png'
image4 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Username2.png'
image5 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\RiotTop.png'
image6 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\logo.png'
image7 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\League_open.png'
image8 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\League.png'
image9 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\VALORANT.png'
image10 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Val.png'
image11 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Valorant_logo.png'
image12 = 'E:\\PROJETOS\\Programming Languages\\Python\\MacroGaming\\Img\\Valorant_open.png'
data_file = 'account_data_LOL.txt'
data_file2 = 'account_data_VAL.txt'
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
    time.sleep(2)
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

def League_Open():
    try:
        img7 = bot.locateCenterOnScreen(image7, confidence=0.7)
        if img7 is not None:
            messagebox.showwarning('Aviso','Seu jogo ja está aberto!')
            return 0
        else:
            raise ImageNotFoundException
    except ImageNotFoundException:
        return 1

root = tk.Tk()
root.title("Minhas contas - League of Legends")
root.geometry("650x370")
root.resizable(width=False, height=False)
imageicon = Image.open(image6)
imageicon = imageicon.resize((64, 64), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(imageicon)
root.iconphoto(False, icon)
application_path = StringVar()
imagetk1 = Image.open(image8)
image_tk1 = ImageTk.PhotoImage(imagetk1)
imagetk2 = Image.open(image10)
image_tk2 = ImageTk.PhotoImage(imagetk2)


def Switch_to_Valorant():
    new_root = Toplevel(root)
    new_root.title("Minhas contas - VALORANT")
    new_root.geometry("650x370")
    new_root.resizable(width=False, height=False)
    imageicon2 = Image.open(image11)
    imageicon2 = imageicon2.resize((64, 64), Image.Resampling.LANCZOS)
    icon2 = ImageTk.PhotoImage(imageicon2)
    new_root.iconphoto(False, icon2)
    root.withdraw()
    new_root.protocol("WM_DELETE_WINDOW", lambda: (root.destroy()))

    def ClickOnValorant():
    
        search = 0
        while search < 60:
            try:
                img5 = bot.locateCenterOnScreen(image5, confidence=0.8)
                img12 = bot.locateCenterOnScreen(image12, confidence=0.7)
                bot.click(img5.x, img5.y)
                time.sleep(0.4)
                bot.click(img12.x, img12.y)
                search = 61
            except:
                search += 1

        if search == 60:
            messagebox.showerror("Erro", "Imagem não encontrada!")
            sys.exit()

    def Valorant_Open():
        try:
            img12 = bot.locateCenterOnScreen(image12, confidence=0.7)
            if img12 is not None:
                messagebox.showwarning('Aviso','Seu jogo ja está aberto!')
                return 0
            else:
                raise ImageNotFoundException
        except ImageNotFoundException:
            return 1

    def load_account_data_valorant():
        if not os.path.exists(data_file2):
            messagebox.showwarning("Aviso", "Arquivo de dados não encontrado. Adicione alguma conta para cria-lo.")
            return

        with open(data_file2, 'r') as file:
            lines = file.readlines()

            if len(lines) >= 1:
                entry_user1_2.insert(0, lines[0].strip()) #0  -> começando na posição 0
            if len(lines) >= 2:
                entry_pass1_2.insert(0, lines[1].strip()) #lines[1] -> seria o número da linha contida no arquivo
            if len(lines) >= 3:
                entry_user2_2.insert(0, lines[2].strip()) #.strip() -> Remove espaços em branco
            if len(lines) >= 4:
                entry_pass2_2.insert(0, lines[3].strip())
            if len(lines) >= 5:
                entry_user3_2.insert(0, lines[4].strip())
            if len(lines) >= 6:
                entry_pass3_2.insert(0, lines[5].strip())
            if len(lines) >= 7:
                entry_user4_2.insert(0, lines[6].strip())
            if len(lines) >= 8:
                entry_pass4_2.insert(0, lines[7].strip())
        
    def save_account_data_valorant():
        with open(data_file2, 'w') as file:
            file.write(entry_user1_2.get() + '\n') #entry_user.get() -> escreve o conteúdo do campo de entrada no arquivo, seguido por um caracter de nova linha '\n'
            file.write(entry_pass1_2.get() + '\n')
            file.write(entry_user2_2.get() + '\n')
            file.write(entry_pass2_2.get() + '\n')
            file.write(entry_user3_2.get() + '\n')
            file.write(entry_pass3_2.get() + '\n')
            file.write(entry_user4_2.get() + '\n')
            file.write(entry_pass4_2.get() + '\n')
        
    def execute_account_valorant(username, password):
        with open(data_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 1:
                value3 = Valorant_Open()
                if value3 == 1:
                    value2 = CallRiot()
                    value = Click(value2)
                    typewrite_account(username, password, value)
                    save_account_data_valorant()
                    ClickOnValorant()
            else:
                messagebox.showerror('Selecione o Riot Client', 'Riot Client não foi selecionado!')
    def load_RiotClient_path_Valorant():
        if os.path.exists(data_path):
            with open(data_path, 'r') as file:
                file_path = file.read().strip()
                if file_path:
                    application_path.set(file_path)
                    label_path_2.config(text="Riot Client pronto!")

    def go_back():
        new_root.destroy()
        root.deiconify()

    label_name = Label(new_root, text='Contas:', font=('Arial 10 bold'))
    label_name.place(x=10, y=10)

    label_footer_main = Label(new_root, text='---------------------------------------------------------------------------------------------------------------------------------------------------------------', font='Arial 10')
    label_footer_main.place(x=5, y=30)

    label_main_game = Label(new_root, text='Jogo selecionado:', font='Arial 10 bold')
    label_main_game.place(x=480, y=200)

    label_user1_2 = Label(new_root, text="Conta 1:")
    label_user1_2.place(x=10, y=60)
    entry_user1_2 = Entry(new_root)
    entry_user1_2.place(x=100, y=60)

    label_pass1_2 = Label(new_root, text="Senha:")
    label_pass1_2.place(x=10, y=85)
    entry_pass1_2 = Entry(new_root, show='*')
    entry_pass1_2.place(x=100, y=85)

    label_user2_2 = Label(new_root, text="Conta 2:")
    label_user2_2.place(x=10, y=140)
    entry_user2_2 = Entry(new_root)
    entry_user2_2.place(x=100, y=140)

    label_pass2_2 = Label(new_root, text="Senha:")
    label_pass2_2.place(x=10, y=165)
    entry_pass2_2 = Entry(new_root, show='*')
    entry_pass2_2.place(x=100, y=165)

    label_user3_2 = Label(new_root, text="Conta 3:")
    label_user3_2.place(x=10, y=220)
    entry_user3_2 = Entry(new_root)
    entry_user3_2.place(x=100, y=220)

    label_pass3_2 = Label(new_root, text="Senha:")
    label_pass3_2.place(x=10, y=245)
    entry_pass3_2 = Entry(new_root, show='*')
    entry_pass3_2.place(x=100, y=245)

    label_user4_2 = Label(new_root, text="Conta 4:")
    label_user4_2.place(x=10, y=300)
    entry_user4_2 = Entry(new_root)
    entry_user4_2.place(x=100, y=300)

    label_pass4_2 = Label(new_root, text="Senha:")
    label_pass4_2.place(x=10, y=325)
    entry_pass4_2 = Entry(new_root, show='*')
    entry_pass4_2.place(x=100, y=325)

    label_path_2 = Label(new_root, text="Riot Client não selecionado.", font='Arial 8 bold')
    label_path_2.place(x=480, y=13)

    button_path = tk.Button(new_root, text="Selecionar RiotClient", command=select_RiotClient, relief='groove')
    button_path.place(x=482, y=70)

    button_league = tk.Button(new_root, text="Contas LOL", relief='groove', command=go_back)
    button_league.place(x=297, y=10)

    label_game = tk.Label(new_root, image=image_tk2)
    label_game.place(x=482, y=232)

    def acc1_val():
        if not entry_user1_2.get() or not entry_pass1_2.get():
            messagebox.showwarning("Aviso", "Usuário ou senha da conta 1 não está registrado.")
            return

        label_name.config(text="Entrando na "+ entry_user1_2.get())
        threading.Thread(target=execute_account_valorant, args=(entry_user1_2.get(), entry_pass1_2.get())).start()

    def acc2_val():
        if not entry_user2_2.get() or not entry_pass2_2.get():
            messagebox.showwarning("Aviso", "Usuário ou senha da conta 2 não está registrado.")
            return

        label_name.config(text="Entrando na "+ entry_user2_2.get())
        threading.Thread(target=execute_account_valorant, args=(entry_user2_2.get(), entry_pass2_2.get())).start()

    def acc3_val():
        if not entry_user3_2.get() or not entry_pass3_2.get():
            messagebox.showwarning("Aviso", "Usuário ou senha da conta 3 não está registrado.")
            return

        label_name.config(text="Entrando na "+ entry_user3_2.get())
        threading.Thread(target=execute_account_valorant, args=(entry_user3_2.get(), entry_pass3_2.get())).start()

    def acc4_val():
        if not entry_user4_2.get() or not entry_pass4_2.get():
            messagebox.showwarning("Aviso", "Usuário ou senha da conta 4 não está registrado.")
            return

        label_name.config(text="Entrando na "+ entry_user4_2.get())
        threading.Thread(target=execute_account_valorant, args=(entry_user4_2.get(), entry_pass4_2.get())).start()

    button1_val = tk.Button(new_root, text="Entrar na Conta 1", command=acc1_val, relief='groove')
    button1_val.place(x=300, y=70)

    button2_val = tk.Button(new_root, text="Entrar na Conta 2", command=acc2_val, relief='groove')
    button2_val.place(x=300, y=152)

    button3_val = tk.Button(new_root, text="Entrar na Conta 3", command=acc3_val, relief='groove')
    button3_val.place(x=300, y=232)

    button4_val = tk.Button(new_root, text="Entrar na Conta 4", command=acc4_val, relief='groove')
    button4_val.place(x=300, y=312)

    load_account_data_valorant()
    load_RiotClient_path_Valorant()
    

label_name = Label(root, text='Contas:', font=('Arial 10 bold'))
label_name.place(x=10, y=10)

label_footer_main = Label(root, text='---------------------------------------------------------------------------------------------------------------------------------------------------------------', font='Arial 10')
label_footer_main.place(x=5, y=30)

label_main_game = Label(root, text='Jogo selecionado:', font='Arial 10 bold')
label_main_game.place(x=480, y=200)

label_user1 = Label(root, text="Conta 1:")
label_user1.place(x=10, y=60)
entry_user1 = Entry(root)
entry_user1.place(x=100, y=60)

label_pass1 = Label(root, text="Senha:")
label_pass1.place(x=10, y=85)
entry_pass1 = Entry(root, show='*')
entry_pass1.place(x=100, y=85)

label_user2 = Label(root, text="Conta 2:")
label_user2.place(x=10, y=140)
entry_user2 = Entry(root)
entry_user2.place(x=100, y=140)

label_pass2 = Label(root, text="Senha:")
label_pass2.place(x=10, y=165)
entry_pass2 = Entry(root, show='*')
entry_pass2.place(x=100, y=165)

label_user3 = Label(root, text="Conta 3:")
label_user3.place(x=10, y=220)
entry_user3 = Entry(root)
entry_user3.place(x=100, y=220)

label_pass3 = Label(root, text="Senha:")
label_pass3.place(x=10, y=245)
entry_pass3 = Entry(root, show='*')
entry_pass3.place(x=100, y=245)

label_user4 = Label(root, text="Conta 4:")
label_user4.place(x=10, y=300)
entry_user4 = Entry(root)
entry_user4.place(x=100, y=300)

label_pass4 = Label(root, text="Senha:")
label_pass4.place(x=10, y=325)
entry_pass4 = Entry(root, show='*')
entry_pass4.place(x=100, y=325)

label_path = Label(root, text="Riot Client não selecionado.", font='Arial 8 bold')
label_path.place(x=480, y=13)

label_game = tk.Label(root, image=image_tk1)
label_game.place(x=482, y=232)

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
            messagebox.showerror('Selecione o Riot Client', 'Riot Client não foi selecionado!')

def select_RiotClient():
    file_path = filedialog.askopenfilename(title="Selecione o Riot Client", filetypes=[("Executáveis", "*.exe")])
    if file_path:
        application_path.set(file_path)
        label_path.config(text="Riot Client pronto!")
        with open(data_path, 'w') as file:
            file.write(file_path)

def load_RiotClient_path():
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            file_path = file.read().strip()
            if file_path:
                application_path.set(file_path)
                label_path.config(text="Riot Client pronto!")

#threading.Thread() -> Cria a thread
#threading.Thread(target=) -> qual função será executada quando a thread iniciar
#threading.Thread(target=... args=) -> contém argumentos que serão passados para a função em 'target'

def acc1():
    if not entry_user1.get() or not entry_pass1.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 1 não está registrado.")
        return

    label_name.config(text="Entrando na "+ entry_user1.get())
    threading.Thread(target=execute_account, args=(entry_user1.get(), entry_pass1.get())).start()

def acc2():
    if not entry_user2.get() or not entry_pass2.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 2 não está registrado.")
        return

    label_name.config(text="Entrando na "+ entry_user2.get())
    threading.Thread(target=execute_account, args=(entry_user2.get(), entry_pass2.get())).start()

def acc3():
    if not entry_user3.get() or not entry_pass3.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 3 não está registrado.")
        return

    label_name.config(text="Entrando na "+ entry_user3.get())
    threading.Thread(target=execute_account, args=(entry_user3.get(), entry_pass3.get())).start()

def acc4():
    if not entry_user4.get() or not entry_pass4.get():
        messagebox.showwarning("Aviso", "Usuário ou senha da conta 4 não está registrado.")
        return

    label_name.config(text="Entrando na "+ entry_user4.get())
    threading.Thread(target=execute_account, args=(entry_user4.get(), entry_pass4.get())).start()

button1 = tk.Button(root, text="Entrar na Conta 1", command=acc1, relief='groove')
button1.place(x=300, y=70)

button2 = tk.Button(root, text="Entrar na Conta 2", command=acc2, relief='groove')
button2.place(x=300, y=152)

button3 = tk.Button(root, text="Entrar na Conta 3", command=acc3, relief='groove')
button3.place(x=300, y=232)

button4 = tk.Button(root, text="Entrar na Conta 4", command=acc4, relief='groove')
button4.place(x=300, y=312)

button_path = tk.Button(root, text="Selecionar RiotClient", command=select_RiotClient, relief='groove')
button_path.place(x=482, y=70)

button_valorant = tk.Button(root, text="Contas VALORANT", relief='groove', command=Switch_to_Valorant)
button_valorant.place(x=297, y=10)

load_account_data()
load_RiotClient_path()

root.mainloop()