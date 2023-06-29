import tkinter as tk
import sys

with open("config/offline.txt", "r", encoding='utf-8') as Change_File:
    Change_Data = Change_File.read()
    Change_Data = Change_Data[0:1]

window = tk.Tk()
window.title("WriterClassic - Offline Mode Switch")
window.geometry("300x70")

label = None

if Change_Data == "1":
    label = tk.Label(window, text="Offline Mode for WriterClassic is enabled!")
elif Change_Data == "0":
    label = tk.Label(window, text="Offline Mode for WriterClassic is disabled!")

def Change_State():
    global Change_File, label, Change_Data
    
    label.destroy()
    
    Change_File = open("config/offline.txt", "w", encoding='utf-8')
    Change_File_2 = open("config/startup.txt", "w", encoding='utf-8')
    
    if Change_Data == "1":
        Change_File.write("0")
        Change_File_2.write("1")
        label = tk.Label(window, text="Offline Mode for WriterClassic has been disabled!")
    elif Change_Data == "0":
        Change_File.write("1")
        Change_File_2.write("0")
        label = tk.Label(window, text="Offline Mode for WriterClassic has been enabled!")
    
    label.pack()
    
    Change_File.close()
    Change_File_2.close()
    
    with open("config/offline.txt", "r", encoding='utf-8') as Change_File:
        Change_Data = Change_File.read()
        Change_Data = Change_Data[0:1]

if sys.platform == "win32":
    window.iconbitmap("data/app_icon.ico")

butt = tk.Button(window, text="Disable/enable Offline Mode for WriterClassic", command=Change_State)
butt.pack()
label.pack()

window.mainloop()