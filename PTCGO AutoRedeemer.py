import tkinter as tk
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener, Controller as KeyboardController
import psutil, pyperclip, sys, time, logging, os, webbrowser
from urllib.request import urlopen

global start_loop
start_loop = False

global CURRENT_VERSION
CURRENT_VERSION = 1.0

''' INIZIO FUNZIONI '''

def on_press(key):
    global start_loop

    logging.info(str(key))
    if str(key) == "Key.enter" and start_loop == True:
        lista_codici = list(str(input_box.get("1.0","end-1c")).split())
        mouse = MouseController()
        keyboard = KeyboardController()
        for codice in lista_codici:
            time.sleep(0.5)
            mouse.position = (427,714)
            mouse.click(Button.left)
            mouse.click(Button.left)
            keyboard.type(str(codice))
            time.sleep(1)
            mouse.position = (426,798)
            mouse.click(Button.left)
            time.sleep(1)
            mouse.position = (950,787)
            mouse.click(Button.left)
            time.sleep(1)
            mouse.position = (657,785)
            mouse.click(Button.left)
            time.sleep(1)
            counter += 1
        start_loop = False
        messagebox.showinfo("PTCGO Autoredeemer", "Task Completed!")
    elif str(key) == "Key.esc":
        exit()
        
listener = Listener(on_press=on_press)
listener.start()

def loadCodes():
    processName = "Pokemon Trading Card Game Online.exe"
    n_codici_ok = None

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                global start_loop
                ''' conto i codici '''
                counter = 0
                lista_codici = list(str(input_box.get("1.0","end-1c")).split())
                for codice in lista_codici:
                    counter += 1
                if counter > 10:
                    n_codici_ok = False
                    messagebox.showerror("PTCGO Autoredeemer", "You can't insert 11 or more codes, PTCGO don't let you redeem them all at once.")
                else:
                    n_codici_ok = True
                    start_loop = True
                    messagebox.showinfo("PTCGO Autoredeemer", "Now open PTCGO, go to the Redeem page and press ENTER to start\n\nIf you want to stop the script press the ESC key.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    if start_loop == False and n_codici_ok == None:
        messagebox.showerror("PTCGO Autoredeemer", "You need to run PTCGO first.")

def showTutorial():
    messagebox.showinfo("Tutorial", "Make sure to write all codes (1 per line) in the box, JUST THE CODES, NO BLANK LINES;" +
    "\n\nDon't enter 10 or more codes, PTCGO client won't let you redeem more than 10 codes at the time;" +
    "\n\nOpen PTCGO and make sure is in fullscreen mode and 1280x720 resolution, otherwise the script won't work;" +
    "\n\nGo to the 'Redeem Code' page;" +
    "\n\nOnce you're ready, press the ENTER key and the script will run, DON'T TOUCH the keyboard or the mouse" +
    "\n\nIf you wish to abort the operation, press the ESC key and the program will close;" +
    "\n\nMake sure your mouse/touchpad is for a RIGHT HAND use." +
    "\n\n------------------------------------------------------------------------"
    "\n\nThanks for using PTCGO Autoredeemer!")

def checkUpdates():
    try:
        versione_letta = urlopen("http://ealf.altervista.org/ptcgored_cur_ver.txt").read()

        if float(versione_letta) > CURRENT_VERSION:
            MsgBox = tk.messagebox.askquestion('PTCGO Autoredeemer','A new version was found! Do you want to download it right now?',icon = 'info')
            if MsgBox == 'yes':
               webbrowser.open("http://ealf.altervista.org/")
            else:
                pass
        else:
            messagebox.showinfo("PTCGO Autoredeemer", "You already have le lastest version.")
    except:
        messagebox.showerror("PTCGO Autoredeemer", "Something went wrong while retriving che lastest version... try later.")
           

''' FINE FUNZIONI '''

window=tk.Tk()
window.title('PTCGO Autoredeemer')
window.geometry("600x550")
window.resizable(False, False)
'''window.iconbitmap(r'icon.ico')'''

title = tk.Label(window, text="PTCGO Autoredeemer v1.0, by xflea")
title.pack(pady = 10)

link = tk.Label(window, text="https://xflea.github.io/", fg="blue", cursor="hand2")
link.pack(pady = 5)
link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))

input_box = tk.Text(window, width = 60, height = 20)
input_box.pack(pady = 10)

btnStart = tk.Button(window, text = "Run Script", bg = "light green", command = loadCodes)
btnStart.pack(pady = 5)

btnTutorial = tk.Button(window, text = "Tutorial", bg = "light blue", command = showTutorial)
btnTutorial.pack(pady = 5)

btnUpdates = tk.Button(window, text = "Check for updates", bg = "light yellow", command = checkUpdates)
btnUpdates.pack(pady = 5)

cur_ver = tk.Label(window, text="Current version: " + str(CURRENT_VERSION))
cur_ver.pack(side = "right")

creditsLab = tk.Label(window, text="Credits to Kiranshastry & Nikita Golubev for the icon idea")
creditsLab.pack(side = "left")

window.mainloop()