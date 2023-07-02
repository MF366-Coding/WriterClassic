import tkinter as tk
import sys

with open("config/startup.txt", "r", encoding='utf-8') as Change_File:
    Change_Data = Change_File.read()
    Change_Data = Change_Data[0:1]

window = tk.Tk()
window.title("WriterClassic - Check for Updates?")
window.geometry("300x70")

label = None

if Change_Data == "1":
    label = tk.Label(window, text="WriterClassic is checking for updates on startup.")
elif Change_Data == "0":
    label = tk.Label(window, text="WriterClassic is not checking for updates on startup.")

def Change_State():
    global Change_File, label, Change_Data
    
    label.destroy()
    
    Change_File = open("config/startup.txt", "w", encoding='utf-8')
    
    if Change_Data == "1":
        Change_File.write("0")
        label = tk.Label(window, text="WriterClassic is not checking for updates on startup.")
    elif Change_Data == "0":
        Change_File.write("1")
        label = tk.Label(window, text="WriterClassic is checking for updates on startup.")
    
    label.pack()
    
    Change_File.close()
    
    with open("config/startup.txt", "r", encoding='utf-8') as Change_File:
        Change_Data = Change_File.read()
        Change_Data = Change_Data[0:1]

if sys.platform == "win32":
    window.iconbitmap("data/app_icon.ico")

butt = tk.Button(window, text="Check for Updates on Startup: Disable/Enable", command=Change_State)
butt.pack()
label.pack()

window.mainloop()