import os
import sys
import tkinter as tk
from tkinter import messagebox as mb

# Plugins for WriterClassic

END = tk.END

if sys.platform == "linux" or sys.platform == "darwin":
    title_1 = "Run with Python 3"
else:
    title_1 = "Run with PATH Python"

def plugin_1(tk_root, tk_text, _file):
    if _file == False:
        mb.showinfo("PythonerClassic", "The file must be saved.")
    elif _file != False and _file.endswith(".py"):
        with open(_file, "r", encoding="utf-8") as filech:
            filez = filech.read()
        if filez == "":
            mb.showinfo("PythonerClassic", "The file musn't be empty.")
        elif filez != "":
            if sys.platform == "win32":
                os.system(f"python {_file}")
            elif sys.platform == "linux" or sys.platform == "darwin":
                os.system(f"python3 {_file}")
    else:
        mb.showinfo("PythonerClassic", "The file must be a non-compiled regular Python file.")
    
title_2 = "No plugin found."
def plugin_2(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")

title_3 = "No plugin found."
def plugin_3(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")

title_4 = "No plugin found."
def plugin_4(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")

title_5 = "No plugin found."
def plugin_5(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")
    
title_6 = "No plugin found."
def plugin_6(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")

title_7 = "No plugin found."
def plugin_7(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")
    
title_backup = "No plugin found."
def plugin_backup(tk_root, tk_text, _file):
    mb.showinfo("Custom Plugins [BETA]", "Plugin not found.")