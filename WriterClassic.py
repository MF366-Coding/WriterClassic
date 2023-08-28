# WriterClassic.py

'''
WriterClassic

Powered by: Python 3.10.11 (in my Windows computer)

The colored menu seems to only work on Linux.
But the app works on Windows and Mac, without the colored menu thought.

Official Repo:
    https://github.com/MF366-Coding/WriterClassic

Find me in this spots:
    https://github.com/MF366-Coding
    https://www.youtube.com/@mf_366
    https://www.buymeacoffee.com/mf366 (Support me please!)

Original idea by: MF366
Fully developed by: MF366

Small but lovely contributions by:
    Norb (norbcodes at GitHub)
    Zeca70 (Zeca70 at GitHub)
'''

NOW_FILE = False

lines = 0

from icecream import ic
from logging_data import _LOG, now
from setting_loader import get_settings, dump_settings

ic.configureOutput(prefix="ic debug statement | -> ")

import os
_PATH = os.path

# Get the absolute path of the script
script_path = _PATH.abspath(__file__)

# Get the directory containing the script
script_dir = _PATH.dirname(script_path)

config = _PATH.join(script_dir, 'config')
user_data = _PATH.join(script_dir, 'user_data')
nix_assets = _PATH.join(script_dir, 'nix_assets')
plugin_dir = _PATH.join(script_dir, 'plugins')
data_dir = _PATH.join(script_dir, 'data')
locale = _PATH.join(script_dir, 'locale')

debug_a = []
debug_a.append(config)
debug_a.append(user_data)
debug_a.append(nix_assets)
debug_a.append(plugin_dir)
debug_a.append(data_dir)
debug_a.append(locale)

import json

from tkinter import Tk, Toplevel, TclError, Label, Button, Text, StringVar, IntVar, Entry, END, Menu, Checkbutton
from tkinter.ttk import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import sys # Platforms and OSes

desktop_win = Tk()
TextWidget = Text(desktop_win, font=("Calibri", 13), borderwidth=5)
TextWidget.pack()

_LOG.write("\n")
_LOG.write(f"{str(now)} - WriterClassic was executed: OK\n")

import random

UNIX_OSES = [
            "darwin",
            "linux",
            "linux2"
        ]

NOT_ALLOWED = [
    "",
    " ",
    "  ",
    "\n",
    "   ",
    "    ",
    "     "
]

settings = get_settings(f"{config}/settings.json")

if not settings["debugging"]:
    ic.disable()

ic(settings)
for debug_b in debug_a:
    ic(debug_a)

startApp = settings["startup"]
if not startApp:
    startApp = "0"
    _LOG.write(f"{str(now)} - Check for updates on startup: DISABLED\n")

elif startApp:
    startApp = "1"
    _LOG.write(f"{str(now)} - Check for updates on startup: ENABLED\n")

else:
    startApp = "1"
    _LOG.write(f"{str(now)} - Check for updates on startup: ENABLED\n")

ic(startApp)

ic(script_dir)
ic(script_path)
ic(f"{data_dir}/logo.png")

# Importing the goodies
from py_compile import compile as _compile
_LOG.write(f"{str(now)} - Imported compile from py_compile: OK\n")

from getpass import getuser
_LOG.write(f"{str(now)} - Imported getuser from getpass: OK\n")

from tkinter import simpledialog as sdg # Inputs with GUI
_LOG.write(f"{str(now)} - Imported simpledialog from tkinter: OK\n")

import tkinter.filedialog as dlg # File Dialogs were never this easy...
_LOG.write(f"{str(now)} - Imported filedialog from tkinter: OK\n")

import tkinter.messagebox as mb # Never gonna give you up... (Pop-ups)
_LOG.write(f"{str(now)} - Imported messagebox from tkinter: OK\n")

from tkinter.font import Font # Ouchie mama (font, daaah)
_LOG.write(f"{str(now)} - Imported Font from tkinter.font: OK\n")

ic(now)

setLang = settings["language"]

ic(setLang)

with open(f'{locale}/'+str(setLang[0:2])+'.wclassic', 'r', encoding='utf-8') as usedLangFile:
    usedLang = usedLangFile.read()
    lang = usedLang.split('\n')
    _LOG.write(f"{str(now)} - Language has been configured correctly: OK\n")

try:
    from simple_webbrowser import simple_webbrowser
    _LOG.write(f"{str(now)} - simple_webbrowser by MF366 has been imported: OK\n")

except (ModuleNotFoundError, ImportError):
    _LOG.write(f"{str(now)} - simple_webbrowser by MF366 has been imported: ERROR\n")
    mb.showerror(lang[155], lang[156])
    module_pip = mb.askyesno(lang[155], lang[157])
    if module_pip:

        if sys.platform == "win32":
            os.system("python -m pip install simple_webbrowser")
            mb.showinfo(lang[155], lang[158])
            _LOG.write(f"{str(now)} - Command 'pip install simple_webbrowser' has been executed: OK\n")
            _LOG.write(f"{str(now)} - End of session\n")
            quit()

        elif sys.platform in UNIX_OSES:
            os.system("pip install simple_webbrowser")
            mb.showinfo(lang[155], lang[158])
            _LOG.write(f"{str(now)} - Command 'pip install simple_webbrowser' has been executed: OK\n")
            _LOG.write(f"{str(now)} - End of session\n")
            quit()

        else:
            mb.showerror(lang[155], f"{lang[159]}\n{lang[160]}")
            _LOG.write(f"{str(now)} - Command 'pip install simple_webbrowser' has been executed: NO (OS ERROR)\n")
            _LOG.write(f"{str(now)} - End of session\n")
            quit()

    elif module_pip == False:
        mb.showerror(lang[155], f"{lang[159]}\n{lang[160]}")
        _LOG.write(f"{str(now)} - Command 'pip install simple_webbrowser' has been executed: NO (USER DECISION)\n")
        _LOG.write(f"{str(now)} - End of session\n")
        quit()

if startApp == "1":
    try:
        from requests import get, exceptions # it's a module yay!
        _LOG.write(f"{str(now)} - requests has been imported: OK\n")
    except (ModuleNotFoundError, ImportError):
        _LOG.write(f"{str(now)} - requests has been imported: ERROR\n")
        mb.showerror(lang[155], lang[156])
        module_pip = mb.askyesno(lang[155], lang[157])
        if module_pip:
            if sys.platform == "win32":
                os.system("python -m pip install requests")
                mb.showinfo(lang[155], lang[158])
                _LOG.write(f"{str(now)} - Command 'pip install requests' has been executed: OK\n")
                _LOG.write(f"{str(now)} - End of session\n")
                quit()
            elif sys.platform in UNIX_OSES:
                os.system("pip install requests")
                mb.showinfo(lang[155], lang[158])
                _LOG.write(f"{str(now)} - Command 'pip install requests' has been executed: OK\n")
                _LOG.write(f"{str(now)} - End of session\n")
                quit()
            else:
                mb.showerror(lang[155], f"{lang[159]}\n{lang[160]}")
                _LOG.write(f"{str(now)} - Command 'pip install requests' has been executed: NO (OS ERROR)\n")
                _LOG.write(f"{str(now)} - End of session\n")
                quit()
        elif module_pip == False:
            mb.showerror(lang[155], f"{lang[159]}\n{lang[160]}")
            _LOG.write(f"{str(now)} - Command 'pip install requests' has been executed: NO (USER DECISION)\n")
            _LOG.write(f"{str(now)} - End of session\n")
            quit()

# Windowing
_LOG.write(f"{str(now)} - WriterClassic launched: OK\n")

if sys.platform == "win32":
    desktop_win.iconbitmap(f"{data_dir}/app_icon.ico")
    _LOG.write(f"{str(now)} - Icon has been changed to WriterClassic's icon [WINDOWS ONLY]: OK\n")

latest_version = None

IGNORE_CHECKING = False

if startApp == '1':
    try:
        response = get('https://api.github.com/repos/MF366-Coding/WriterClassic/releases/latest', timeout=3.5)
        _LOG.write(f"{str(now)} - Connected to GitHub: OK\n")
        data = json.loads(response.text)
        _LOG.write(f"{str(now)} - Got WriterClassic Releases data: OK\n")
        latest_version = data['tag_name']
        _LOG.write(f"{str(now)} - Got the latest release's tag: OK\n")

    except (exceptions.ConnectTimeout, exceptions.ConnectionError, TimeoutError, exceptions.ReadTimeout):
        mb.showerror(lang[148], f"{lang[135]}\n{lang[136]}")
        _LOG.write(f"{str(now)} - Connected to GitHub: ERROR\n")
        _LOG.write(f"{str(now)} - Connection has timed out, is restricted or is simply unavailable: INFO\n")
        IGNORE_CHECKING = True
        _LOG.write(f"{str(now)} - WriterClassic is launching without checking for updates: OK\n")

ic(IGNORE_CHECKING)
ic(latest_version)

# Config files
appV = "v8.7.0"
advV ="v8.7.0.195-r"

ic(appV)
ic(advV)

theme = settings["theme"]

ic(theme)

_LOG.write(f"{str(now)} - Got the current theme: OK\n")

font_use = settings["font"]
_LOG.write(f"{str(now)} - Got the current font family/type: OK\n")
_LOG.write(f"{str(now)} - Got the current font size: OK\n")

def fast_dump():
    dump_settings(f"{config}/settings.json", settings)

# Windowing... again
if NOW_FILE == False:
    desktop_win.title(lang[1])

_LOG.write(f"{str(now)} - Window's title was set to WriterClassic: OK\n")

try:
    FontSet = Font(family=font_use["type"], size=font_use["size"])
    __font_type = font_use["type"]
    __font_size = font_use["size"]
    _LOG.write(f"{str(now)} - Font size is {str(__font_size)}: OK\n")
    _LOG.write(f"{str(now)} - Font family/type is {str(__font_type)}: OK\n")

except TclError:
    mb.showerror(lang[149], f"{lang[144]}\n{lang[145]}\n{lang[146]}")
    _LOG.write(f"{str(now)} - Font size is set to 14 because of a font error: OK\n")
    FontSet = Font(family="Segoe UI", size=14)
    _LOG.write(f"{str(now)} - Font type is set to Segoe UI because of a font error: OK\n")
    settings["font"] = {
        "type": "Segoe UI",
        "size": 14
    }

    fast_dump()


_LOG.write(f"{str(now)} - The editing interface has been created: OK\n")

geomValue = settings["geometry"]
_LOG.write(f"{str(now)} - Got the window's dimensions settings: OK\n")
GeomValues = geomValue.split('x')

try:
    desktop_win.geometry(geomValue)
    _LOG.write(f"{str(now)} - Applied the window's dimensions: OK\n")
except TclError:
    desktop_win.geometry("700x500")
    GeomValues = [700, 500]
    _LOG.write(f"{str(now)} - Applied the window's dimensions: ERROR\n")
    _LOG.write(f"{str(now)} - Reverted to 700x500: OK\n")
    mb.showerror(lang[166], f"{lang[167]}\n{lang[168]}")

try:
    TextWidget.configure(bg=theme["color"], fg=theme["fg"], width=int(GeomValues[0]), height=int(GeomValues[1]), insertbackground=theme["ct"], font=FontSet)
    _LOG.write(f"{str(now)} - Applied configurations to the editing interface: OK\n")

except TclError:
    _LOG.write(f"{str(now)} - Applied configurations to the editing interface: ERROR\n")
    mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
    TextWidget.configure(bg="black", fg="white", width=int(GeomValues[0]), height=int(GeomValues[1]), insertbackground="white", font=FontSet)
    _LOG.write(f"{str(now)} - Reconfigured the editing interface: OK\n")

_LOG.write(f"{str(now)} - 'Packed' the editing interface: OK\n")

# Defining the menu bar
menu_bar = Menu(desktop_win)
_LOG.write(f"{str(now)} - Created the menu bar: OK\n")

try:
    if sys.platform == "linux":
        menu_bar.configure(background=theme["menu"], foreground=theme["mfg"])
        _LOG.write(f"{str(now)} - Applied the theme to the menu bar: OK\n")
except TclError:
    if sys.platform == "linux":
        _LOG.write(f"{str(now)} - Applied the theme to the menu bar: ERROR\n")
        mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_bar.configure(background="white", foreground="black")
        _LOG.write(f"{str(now)} - Applied the light theme to the menu bar as last resource: OK\n")

ic(sys.platform)

if settings["advanced-mode"]:
    ADVANCED = True

else:
    ADVANCED = False

ic(ADVANCED)

menu_1 = Menu(menu_bar)
menu_2 = Menu(menu_1)
menu_3 = Menu(menu_2)
menu_4 = Menu(menu_1)
menu_5 = Menu(menu_4)
menu_6 = Menu(menu_4)
menu_7 = Menu(menu_1)
menu_8 = Menu(menu_bar)
menu_9 = Menu(menu_8)
menu_10 = Menu(menu_bar)
menu_11 = Menu(menu_bar)
menu_12 = Menu(menu_bar)
menu_13 = Menu(menu_12)

if ADVANCED:
    menu_14 = Menu(menu_bar)

_LOG.write(f"{str(now)} - Created all the menus: OK\n")

def writeStartup(text: bool):
    settings["startup"] = text
    fast_dump()
    _LOG.write(f"{str(now)} - Check for updates on Startup (True - 1/False - 0) has been changed to {text}: OK\n")

# Check for Updates
class UpdateCheck:
    @staticmethod
    def check_other():
        """
        check_other checks for updates on startup only
        """

        if appV != latest_version and IGNORE_CHECKING == False:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            _LOG.write(f"{str(now)} - Versions don't match: WARNING\n")
            if askForUpdate:
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')
                _LOG.write(f"{str(now)} - Went to the latest release at GitHub: OK\n")

        elif IGNORE_CHECKING == True:
            _LOG.write(f"{str(now)} - Couldn't check for updates on startup: WARNING\n")
            pass

    @staticmethod
    def check():
        """
        check checks for updates whenever the user clicks Check for Updates
        """

        if appV != latest_version and IGNORE_CHECKING == False:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                _LOG.write(f"{str(now)} - Went to the latest release at GitHub: OK\n")
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')

        elif appV == latest_version and IGNORE_CHECKING == False:
            mb.showinfo(title=lang[93], message=lang[92])
            _LOG.write(f"{str(now)} - Versions match | WriterClassic is up to date: OK\n")

        else:
            mb.showerror(lang[148], f"{lang[135]}\n{lang[136]}")
            _LOG.write(f"{str(now)} - Couldn't check for updates (Bad Internet, Connection Timeout, Restricted Internet): WARNING\n")

    @staticmethod
    def change():
        if startApp == '1':
            writeStartup(False)
            mb.showinfo(title=lang[1], message=lang[101])
            _LOG.write(f"{str(now)} - Check for updates on startup has been disabled: OK\n")
        else:
            writeStartup(True)
            mb.showinfo(title=lang[1], message=lang[101])
            _LOG.write(f"{str(now)} - Check for updates on startup has been enabled: OK\n")

if startApp == '1':
    UpdateCheck.check_other()
    _LOG.write(f"{str(now)} - Checked for updates on startup: AWAITING REPLY\n")

# Windowing... one more time...
def SetWinSize():
    widthSet = sdg.askinteger(lang[1], lang[57])
    _LOG.write(f"{str(now)} - Got a width value: AWAITING FOR ANTI-BUG CHECK\n")
    if widthSet in NOT_ALLOWED:
        mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        _LOG.write(f"{str(now)} - Got a width value: ERROR (ILLEGAL VALUE)\n")

    elif widthSet not in NOT_ALLOWED:
        _LOG.write(f"{str(now)} - Got a width value: OK\n")
        heightSet = sdg.askinteger(lang[1], lang[58])
        _LOG.write(f"{str(now)} - Got a height value: AWAITING FOR ANTI-BUG CHECK\n")

        if heightSet in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
            _LOG.write(f"{str(now)} - Got a width value: ERROR (ILLEGAL VALUE)\n")

        elif heightSet not in NOT_ALLOWED:
            _LOG.write(f"{str(now)} - Got a width value: OK\n")
            TextWidget.configure(width=widthSet, height=heightSet)
            _LOG.write(f"{str(now)} - Editing interface has been reconfigured: OK\n")
            desktop_win.geometry(str(widthSet)+'x'+str(heightSet))
            _LOG.write(f"{str(now)} - Window's dimensions were set: OK\n")

            _LOG.write(f"{str(now)} - Configured default window's dimensions: OK\n")
            settings["geometry"] = str(widthSet)+'x'+str(heightSet)
            fast_dump()

# Theme Picker
def ThemeSet(colour_first, colour_second, colour_third, colour_fourth, colour_fifth):
    settings["theme"] = {
        "color":str(colour_first),
        "ct":str(colour_third),
        "fg":str(colour_second),
        "mfg":str(colour_fifth),
        "menu":str(colour_fourth)
    }

    fast_dump()

    TextWidget.configure(bg=colour_first, fg=colour_second, insertbackground=colour_third)
    _LOG.write(f"{str(now)} - Editing interface has been reconfigured: OK\n")

    TextWidget.pack()

    waitResponse = mb.askyesno(parent=desktop_win, title=lang[30], message=lang[31])
    _LOG.write(f"{str(now)} - Asked for app restart: AWAITING RESPONSE\n")

    if waitResponse:
        desktop_win.destroy()
        _LOG.write(f"{str(now)} - End of session: QUIT\n")

    else:
        _LOG.write(f"{str(now)} - Cancel/No as response: OK\n")

# ragequit
def quickway():
    _LOG.write(f"{str(now)} - End of session: QUIT\n")
    desktop_win.destroy()

# Setup (Lang files)
def LanguageSet(language_set, root_win):
    settings["language"] = language_set
    _LOG.write(f"{str(now)} - A new language has been set ({str(language_set)}): OK\n")
    fast_dump()

    popup_define = mb.askyesno(parent=root_win, title=lang[30], message=lang[31])
    _LOG.write(f"{str(now)} - Asked for app restart: AWAITING RESPONSE\n")
    if popup_define:
        root_win.destroy()
        _LOG.write(f"{str(now)} - End of session: QUIT\n")
    else:
        _LOG.write(f"{str(now)} - Cancel/No as response: OK\n")

# Notepad
def new_window():
    newWindow = Toplevel(desktop_win)
    _LOG.write(f"{str(now)} - A new window has been called: AWAITING CONFIGURATION\n")

    # Windowing... yet once more LMAO...
    newWindow.title(lang[22])
    newWindow.geometry("600x400")

    TextWidget2 = Text(newWindow, borderwidth=5)

    TextWidget2.configure(bg=theme["color"], fg=theme["fg"], width=GeomValues[0], height=GeomValues[1], insertbackground=theme["ct"], font=FontSet)
    TextWidget2.pack()

    _LOG.write(f"{str(now)} - Notes Plugin's window has been fully configured: OK\n")

    newWindow.mainloop()

def DOC_STATS():
    global lines

    _data = TextWidget.get(0.0, END)
    _LOG.write(f"{str(now)} - Extracted text from the editing interface: OK\n")

    if _data in NOT_ALLOWED:
        lines = 0
        _LOG.write(f"{str(now)} - There were {str(lines)} lines: INFO (EMPTY FILE)\n")

    else:
        _lines = _data.split("\n")
        y_lines = list(filter(("").__ne__, _lines))
        x_lines = int(len(y_lines))
        lines = x_lines
        _LOG.write(f"{str(now)} - There were {str(lines)} lines: OK\n")

    mb.showinfo(lang[164], f"{lang[165]}: {str(lines)}")

# Repo
def repo():
    ourRepo = "https://github.com/MF366-Coding/WriterClassic/"

    simple_webbrowser.Website(ourRepo)
    _LOG.write(f"{str(now)} - Opened the repository: AWAITING FOR FUNCTION OR ERROR\n")

# Clock
def clockPlugin():
    clockWindow = Toplevel(desktop_win)
    clockWindow.geometry('275x65')
    clockWindow.resizable(False, False)
    _LOG.write(f"{str(now)} - A new window has been called: AWAITING CONFIGURATION\n")

    #Windowing
    clockWindow.title(lang[23])

    TextWidget2 = Label(clockWindow)

    TextWidget2.configure(text=datetime.datetime.now())
    TextWidget2.configure(
        font=(100)
        )

    _LOG.write(f"{str(now)} - Clock Plugin's window has been configured: OK\n")

    TextWidget.pack()
    clockWindow.mainloop()

# Text font
def fontEdit(winType):
    if winType == 1:
        fontSize = sdg.askinteger(lang[59], lang[60], minvalue=1)
        if fontSize in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif fontSize not in NOT_ALLOWED:
            font_use["size"] = fontSize
            settings["font"]["size"] = fontSize
            fast_dump()
            _LOG.write(f"{str(now)} - Font size has been changed to {str(fontSize)}: OK\n")
            mb.showinfo(lang[1], lang[63])
    else:
        fontType = sdg.askstring(lang[61], lang[62])
        if fontType in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif fontType not in NOT_ALLOWED:
            font_use["type"] = fontType
            settings["font"]["type"] = fontType
            fast_dump()
            _LOG.write(f"{str(now)} - Font type has been changed to {str(fontType)}: OK\n")
            mb.showinfo(lang[1], lang[63])

# clears the screen
def newFile():
    global NOW_FILE

    desktop_win.title(lang[1])
    TextWidget.delete(index1=0.0, index2=END)
    NOW_FILE = False

    _LOG.write(f"{str(now)} - A new file has been created: OK\n")

    ic(NOW_FILE)


file_types = [(lang[32], '*.txt'),
              (lang[33], '*.config'),
              (lang[34], '*.css'),
              (lang[35], '*.csv'),
              (lang[36], '*.html'),
              (lang[37], '*.inf'),
              (lang[38], '*.info'),
              (lang[39], '*.ini'),
              (lang[40], '*.js'),
              (lang[41], '*.py'),
              (lang[42], '*.log'),
              (lang[43], '*.xml'),
              (lang[44], '*.1st'),
              (lang[45], '*.a'),
              (lang[46], '*.a8s'),
              (lang[47], '*.ans'),
              (lang[48], '*.arena'),
              (lang[49], '*.as'),
              (lang[50], '*.asa'),
              (lang[51], '*.asm'),
              (lang[52], '*.md'),
              (lang[102], '*.json'),
              (lang[185], '*.wclassic'),
              (lang[110], '*.ath'),
              (lang[111], "*.att"),
              (lang[112], "*.avs"),
              (lang[113], "*.bbz"),
              (lang[114], "*.bcs"),
              (lang[115], "*.bmk"),
              (lang[116], "*.book"),
              (lang[117], "*.bpw"),
              (lang[118], "*.bsd"),
              (lang[119], "*.bsdl"),
              (lang[120], "*.bsh"),
              (lang[121], "*.camp"),
              (lang[122], "*.cel"),
              (lang[123], "*.celx"),
              (lang[124], "*.cgi"),
              (lang[127], "*.*")
              ]

_LOG.write(f"{str(now)} - Filetypes have been configured correctly: OK\n")

# opens a file
def OpenFile(root_win):
    """
    OpenFile opens a file selected from the following interface

    Args:
        root_win (Tk): WriterClassic's main window
    """
    global NOW_FILE

    file_path = dlg.asksaveasfilename(parent=root_win, filetypes=file_types, defaultextension="*.*", initialfile="Open a File", confirmoverwrite=False, title=lang[7])

    # Get the selected file extension
    selected_extension = None
    for ft in file_types:
        if file_path.lower().endswith(ft[1]):
            selected_extension = ft[1]
            break

    # Append the selected extension if not already included
    if selected_extension and not file_path.lower().endswith(selected_extension):
        file_path += selected_extension

    try:
        file_input = open(file_path, "rt", encoding="utf-8")
        file_data = file_input.read()

        root_win.title(f"{lang[1]} - {file_path}")
        TextWidget.delete(index1=0.0, index2=END)
        TextWidget.insert(chars=file_data, index=0.0)

        _LOG.write(f"{str(now)} - A file at the path {str(file_path)} has been opened: OK\n")

        NOW_FILE = str(file_path)
        file_input.close()

    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
        mb.showerror(title=lang[187], message=f"{lang[188]} {str(file_path)}.")
        run_default = mb.askyesno(title=lang[187], message=lang[189])
        if run_default:
            os.system(str(file_path))

    finally:
        ic(NOW_FILE)

# Saving as
def SaveFile(root_win):
    global NOW_FILE

    dados = TextWidget.get(0.0, END)
    file_path = dlg.asksaveasfilename(parent=root_win, title=lang[9], confirmoverwrite=True, filetypes=file_types, defaultextension="*.*", initialfile="New File To Save")

    # Get the selected file extension
    selected_extension = None
    for ft in file_types:
        if file_path.lower().endswith(ft[1]):
            selected_extension = ft[1]
            break

    # Append the selected extension if not already included
    if selected_extension and not file_path.lower().endswith(selected_extension):
        file_path += selected_extension

    file = open(file_path, "wt", encoding='utf-8')
    file.write(str(dados))
    file.close()
    mb.showinfo(lang[1], lang[101])
    root_win.title(f"{lang[1]} - {file_path}")

    _LOG.write(f"{str(now)} - A file has been saved as {str(file_path)}: OK\n")

    NOW_FILE = str(file_path)
    ic(NOW_FILE)

def Save(root_win):
    global NOW_FILE

    if NOW_FILE == False:
        SaveFile(root_win=root_win)

    elif NOW_FILE != False:
        data = TextWidget.get(0.0, END)

        file_path = NOW_FILE
        file = open(file_path, "wt", encoding='utf-8')
        file.write(str(data))
        file.close()
        mb.showinfo(lang[1], lang[101])
        root_win.title(f"{lang[1]} - {file_path}")

        _LOG.write(f"{str(now)} - An existing file has been saved over ({str(file_path)}): OK\n")

        NOW_FILE = str(file_path)
        ic(NOW_FILE)

# Whatever... (File Eraser)
def WipeFile(root_win):
    sureConfirm = mb.askyesno(title=lang[55], message=lang[56])
    if sureConfirm:
        file_path = dlg.asksaveasfilename(parent=root_win, confirmoverwrite=False, filetypes=file_types, defaultextension="*.*", initialfile="File to Wipe")

        # Get the selected file extension
        selected_extension = None
        for ft in file_types:
            if file_path.lower().endswith(ft[1]):
                selected_extension = ft[1]
                break

        # Append the selected extension if not already included
        if selected_extension and not file_path.lower().endswith(selected_extension):
            file_path += selected_extension

        file_input = open(file_path, "wt", encoding="utf-8")
        file_input.write('')
        mb.showinfo(title=lang[1], message=lang[101])

        _LOG.write(f"{str(now)} - A file has been wiped at {str(file_path)}: OK\n")

        root_win.title(lang[1])
        file_input.close()

desktop_entry = None

def desktop_create(pycommand: str):
    """
    desktop_create creates a Desktop File for Linux

    Args:
        pycommand (string): The command/alias for Python (example: pycommand='python3')
    """

    global desktop_entry

    desktop_entry = f"""#!/usr/bin/env xdg-open
[Desktop Entry]
Name=WriterClassic
Categories=Utility;Office;
Comment[pt_PT]=Editor de ficheiros de texto plano
Comment=Plain text editor
Exec={pycommand} {script_path}
GenericName[pt_PT]=Editor de Texto
GenericName=Text Editor
Icon={data_dir}/logo.png
InitialPreference=8
Keywords[pt_PT]=texto;txt;editor;nota;bloco de notas;wclassic;
Keywords=text;txt;editor;note;notepad;wclassic;
MimeType=text/plain;
Path=
StartupNotify=true
StartupWMClass=WriterClassic
Terminal=false
TerminalOptions=
Type=Application
X-DBUS-ServiceName=
X-DBUS-StartupType=Multi
X-DocPath=
X-KDE-SubstituteUID=false
X-KDE-Username=
"""

    with open(f"{script_dir}/WriterClassic.desktop", mode="w", encoding='utf-8') as desktop_file:
        desktop_file.write(desktop_entry)
        mb.showinfo(lang[1], lang[101])
        desktop_file.close()

    ic(desktop_entry)


def desktop_create_win():
    """
    desktop_create_win creates the window that later on calls desktop_create

    No args needed or wanted.
    """
    desktop_created_win = Toplevel(desktop_win)
    desktop_created_win.title(lang[197])
    if sys.platform == "win32":
        desktop_created_win.iconbitmap(f"{data_dir}/app_icon.ico")
    desktop_created_win.geometry("600x150")
    desktop_created_win.resizable(False, False)

    LabA = Label(desktop_created_win, text=lang[193], font=("Segoe UI", 15))
    LabB = Label(desktop_created_win, text=lang[194], font=("Segoe UI", 12))
    ButtA = Button(desktop_created_win, text=lang[196], command=lambda:
        desktop_create(pycommand='python3'))
    ButtB = Button(desktop_created_win, text=lang[195], command=lambda:
        desktop_create(pycommand='python'))

    LabA.pack()
    LabB.pack()
    ButtA.pack()
    ButtB.pack()

# credits
def appCredits():
    mb.showinfo(title=lang[28], message=lang[65])
    _LOG.write(f"{str(now)} - The Credits have been shown: OK\n")

# easter egg super secret!
def surprise_egg():
    askNow = sdg.askstring(lang[29], lang[66])

    if askNow == 'Nice stuff!!':
        simple_webbrowser.Website('https://www.youtube.com/watch?v=W6FG7yVUaKQ')
        ic()

    elif askNow == 'Scan':
        mb.showwarning("Your PC has virus!", "Press Alt+F4 to remove all viruses!!!\nDo it!!!")
        ic()

    elif askNow == "":
        ic()
        return None

    else:
        mb.showerror(lang[29], lang[67])
        ic()

# help me pls!!!
def APP_HELP():
    simple_webbrowser.Website("https://github.com/MF366-Coding/WriterClassic#help")
    _LOG.write(f"{str(now)} - Requested online help: AWAITING FOR CONNECTION\n")
    ic()

# infoooooo
def aboutApp():
    with open(f"{data_dir}/about.wclassic", mode="r", encoding='utf-8') as about_d:
        about_data = about_d.read()

    about_dialogue = Toplevel(desktop_win)
    about_dialogue.geometry("600x250")

    about_dialogue.resizable(False, False)

    about_dialogue.title(lang[64])
    label_1 = Label(about_dialogue, text=str(about_data), font=("Calibri", 13))

    from PIL import Image, ImageTk

    # Load the PNG image using PIL
    image = Image.open(f"{data_dir}/logo.png")

    # Get the dimensions of the image
    image_width, image_height = image.size

    # Define the maximum width and height for the resized image
    max_width = 200
    max_height = 200

    # Calculate the desired dimensions while maintaining the aspect ratio
    if image_width > image_height:
        # Calculate the desired width based on the maximum width
        desired_width = min(image_width, max_width)
        # Calculate the corresponding height
        desired_height = int(desired_width * image_height / image_width)
    else:
        # Calculate the desired height based on the maximum height
        desired_height = min(image_height, max_height)
        # Calculate the corresponding width
        desired_width = int(desired_height * image_width / image_height)

    # Resize the image
    resized_image = image.resize((desired_width, desired_height), Image.LANCZOS)

    # Create a PhotoImage object from the resized image
    photo = ImageTk.PhotoImage(resized_image)

    button_1 = Button(about_dialogue, text="Ok", command=about_dialogue.destroy)
    button_2 = Button(about_dialogue, text="WriterClassic Website", command=lambda:
        simple_webbrowser.webbrowser.open("https://mf366-coding.github.io/writerclassic.html", new=2))

    # Create a Label widget to display the image
    image_label = Label(about_dialogue, image=photo)

    image_label.grid(column=1, row=1)
    label_1.grid(column=2, row=1)
    button_1.grid(column=1, row=2)
    button_2.grid(column=2, row=2)

    about_dialogue.mainloop()

    _LOG.write(f"{str(now)} - The About dialogue has been shown\n")
    about_d.close()

    ic()

def Tips_Tricks():
    picked_text = random.choice((
        lang[140],
        lang[141],
        lang[142],
        lang[143]
    ))

    mb.showinfo(lang[1], picked_text)
    _LOG.write(f"{str(now)} - Requested Tips & Tricks: OK\n")

    ic()

def resetWriter(*args):
    global settings

    askSOS = mb.askyesno(lang[77], lang[78])
    if askSOS:
        settings = {
            "font": {
                "type": "Segoe UI",
                "size": 13
            },

            "theme": {
                "color": "black",
                "ct": "white",
                "fg": "white",
                "mfg": "black",
                "menu": "dark grey"
            },

            "advanced-mode": False,

            "startup": True,

            "geometry": "700x500",

            "language": "en",

            "dencrypt": "",

            "debugging": False,
            
            "email": ""
        }

        fast_dump()

        _LOG.write(f"{str(now)} - Fonts have been reset: OK\n")

        _LOG.write(f"{str(now)} - Language and theme have both been reset: OK\n")

        desktop_win.geometry('700x500')

        _LOG.write(f"{str(now)} - Window's dimensions have been reset: OK\n")

        with open(f"{config}/signature.wclassic", "w", encoding='utf-8') as sigFILE:
            sigFILE.write("--\nBest regards,\nThis is a customizable signature in a file named signature.wclassic in the data folder...")
            _LOG.write(f"{str(now)} - The Custom Signature has been reset: OK\n")

    ic(settings)

def _terminal_get(entry_selection):
    _data = entry_selection.get()

    os.system(_data)

    _LOG.write(f"{str(now)} - Used the following command on the Terminal - {str(_data)}: OK\n")

    ic(_data)

def _trick_terminal(func, window):
    window.destroy()

    func()

    _LOG.write(f"{str(now)} - Refreshed the Terminal Inputs: OK\n")

def Terminal():
    terminal = Toplevel(desktop_win)

    terminal.title(lang[183])

    _LOG.write(f"{str(now)} - Opened the Terminal Inputs: OK\n")

    entry_1 = Entry(terminal, font=("Calibri", 13))
    butt_1 = Button(terminal, text=lang[178], command=lambda:
        _terminal_get(entry_1))
    butt_2 = Button(terminal, text=lang[184], command=lambda:
        _trick_terminal(Terminal, terminal))

    entry_1.pack()
    butt_1.pack()
    butt_2.pack()

    terminal.mainloop()


class InternetOnWriter:
    @staticmethod
    def Website():
        askForLink = sdg.askstring(lang[80], lang[91])
        if askForLink != ' ' or askForLink != '':
            simple_webbrowser.Website(askForLink)
            _LOG.write(f"{str(now)} - Went to {str(askForLink)} via WriterClassic: OK\n")
        ic()

    @staticmethod
    def Search(engine):
        if engine == 'google':
            askForTyping = sdg.askstring(lang[83], lang[90])
            if askForTyping != '':
                simple_webbrowser.Google(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Google: OK\n")

        elif engine == 'bing':
            askForTyping = sdg.askstring(lang[82], lang[90])
            if askForTyping != '':
                simple_webbrowser.Bing(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Bing: OK\n")

        elif engine == 'ysearch':
            # stands for Yahoo!
            askForTyping = sdg.askstring(lang[85], lang[90])
            if askForTyping != '':
                simple_webbrowser.Yahoo(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Yahoo!: OK\n")

        elif engine == 'ddgo':
            # stands for DuckDuckGo
            askForTyping = sdg.askstring(lang[84], lang[90])
            if askForTyping != '':
                simple_webbrowser.DuckDuckGo(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on DuckDuckGo: OK\n")

        elif engine == "yt":
            # stands for YouTube
            askForTyping = sdg.askstring(lang[99], lang[90])
            if askForTyping != '':
                simple_webbrowser.YouTube(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on YouTube: OK\n")

        elif engine == "ecosia":
            askForTyping = sdg.askstring(lang[98], lang[90])
            if askForTyping != '':
                simple_webbrowser.Ecosia(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Ecosia: OK\n")

        elif engine == "stack":
            # stands for Stack Overflow
            askForTyping = sdg.askstring(lang[100], lang[90])
            if askForTyping != '':
                simple_webbrowser.StackOverflow(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on StackOverflow: OK\n")

        elif engine == "soundcloud":
            askForTyping = sdg.askstring(lang[104], lang[90])
            if askForTyping != '':
                simple_webbrowser.SoundCloud(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on SoundCloud: OK\n")

        elif engine == "archive":
            # stands for The Internet Archive
            askForTyping = sdg.askstring(lang[109], lang[90])
            if askForTyping != '':
                simple_webbrowser.Archive(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on The Internet Archive: OK\n")

        elif engine == "qwant":
            # stands for Qwant.com
            askForTyping = sdg.askstring(lang[108], lang[90])
            if askForTyping != '':
                simple_webbrowser.Qwant(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Qwant: OK\n")

        elif engine == "spotify":
            # stands for Spotify Online
            askForTyping = sdg.askstring(lang[126], lang[90])
            if askForTyping != '':
                simple_webbrowser.SpotifyOnline(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Spotify Online: OK\n")

        elif engine == 'brave':
            # stands for Brave Search
            askForTyping = sdg.askstring(lang[139], lang[90])
            if askForTyping != '':
                simple_webbrowser.Brave(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on Brave Search: OK\n")

        elif engine == "github":
            askForTyping = sdg.askstring(lang[170], lang[90])
            if askForTyping != '':
                simple_webbrowser.GitHub(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on GitHub: OK\n")

        elif engine == "gitlab":
            askForTyping = sdg.askstring(lang[172], lang[90])
            if askForTyping != '':
                simple_webbrowser.GitLab(askForTyping)
                _LOG.write(f"{str(now)} - Searched for {str(askForTyping)} on GitLab: OK\n")

def lock_a_win(window, _type: bool):
    if _type:
        window.resizable(False, False)
    elif _type == False:
        window.resizable(True, True)

def plugin_help():
    simple_webbrowser.Website("https://github.com/MF366-Coding/WriterClassic/wiki/Plugin-Setup")
    _LOG.write(f"{str(now)} - Requested help with the Plugin Central: OK\n")

def article_md():
    simple_webbrowser.Website(url='https://github.com/MF366-Coding/WriterClassic/wiki/Manual-Configuration-Setup')
    _LOG.write(f"{str(now)} - Requested help with the Manual Configuration: OK\n")


class PluginCentral:
    def __init__(self, window):
        self.window = window
        self.add_atributes()
        self.window.mainloop()

    def _open_plugin(self, module):
        if module == 1:
            try:
                from plugins import _1

                _confirm = mb.askyesno(lang[174], f"{lang[178]} ({_1.title})?")

                if _confirm:
                    _1.plugin(desktop_win, TextWidget, NOW_FILE)
                    _LOG.write(f"{str(now)} - Plugin 1 was executed: OK\n")

            except Exception:
                mb.showerror(lang[161], lang[162])

        elif module == 2:
            try:
                from plugins import _2

                _confirm = mb.askyesno(lang[174], f"{lang[178]} ({_2.title})?")

                if _confirm:
                    _2.plugin(desktop_win, TextWidget, NOW_FILE)
                    _LOG.write(f"{str(now)} - Plugin 2 was executed: OK\n")

            except Exception:
                mb.showerror(lang[161], lang[162])

        elif module == 3:
            try:
                from plugins import _3

                _confirm = mb.askyesno(lang[174], f"{lang[178]} ({_3.title})?")

                if _confirm:
                    _3.plugin(desktop_win, TextWidget, NOW_FILE)
                    _LOG.write(f"{str(now)} - Plugin 3 was executed: OK\n")

            except Exception:
                mb.showerror(lang[161], lang[162])

        elif module == 4:
            try:
                from plugins import _4

                _confirm = mb.askyesno(lang[174], f"{lang[178]} ({_4.title})?")

                if _confirm:
                    _4.plugin(desktop_win, TextWidget, NOW_FILE)
                    _LOG.write(f"{str(now)} - Plugin 4 was executed: OK\n")

            except Exception:
                mb.showerror(lang[161], lang[162])

    def add_atributes(self):
        self.window.title(lang[174])
        self.window.geometry("500x85")
        self.window.resizable(False, False)

        if sys.platform == "win32":
            self.window.iconbitmap(f"{data_dir}/app_icon.ico")

        try:
            from plugins import _1

            butt_1 = Button(self.window, text=f"{lang[175]} | {_1.title}", command=lambda:
                self._open_plugin(1))
            butt_1.grid(column=1, row=1)

        except Exception:
            butt_1 = Button(self.window, text=f"{lang[175]} | Title not found", command=lambda:
                self._open_plugin(1))
            butt_1.grid(column=1, row=1)


        try:
            from plugins import _2

            butt_2 = Button(self.window, text=f"{lang[176]} | {_2.title}", command=lambda:
                self._open_plugin(2))
            butt_2.grid(column=2, row=1)

        except Exception:
            butt_2 = Button(self.window, text=f"{lang[176]} | Title not found", command=lambda:
                self._open_plugin(2))
            butt_2.grid(column=2, row=1)


        try:
            from plugins import _3

            butt_3 = Button(self.window, text=f"{lang[177]} 3 | {_3.title}", command=lambda:
                self._open_plugin(3))
            butt_3.grid(column=1, row=2)

        except Exception:
            butt_3 = Button(self.window, text=f"{lang[177]} 3 | Title not found", command=lambda:
                self._open_plugin(3))
            butt_3.grid(column=1, row=2)


        try:
            from plugins import _4

            butt_4 = Button(self.window, text=f"{lang[177]} 4 | {_4.title}", command=lambda:
                self._open_plugin(4))
            butt_4.grid(column=2, row=2)

        except Exception:
            butt_4 = Button(self.window, text=f"{lang[177]} 4 | Title not found", command=lambda:
                self._open_plugin(4))
            butt_4.grid(column=2, row=2)


        _LOG.write(f"{str(now)} - The Plugin Central has been created: OK\n")


def clear_log_screen(text_interface):
    text_interface.delete(0.0, END)

    with open(f"{user_data}/log.wclassic", "r", encoding="utf-8") as _TEMP_LOG:
        temp_log = _TEMP_LOG.read()
        text_interface.insert(0.0, str(temp_log))
        _TEMP_LOG.close()

    _LOG.write(f"{str(now)} - Log File has been refreshed: OK\n")


def show_log():
    _new_window = Toplevel(desktop_win)
    _new_window.resizable(False, False)
    _new_editor = Text(_new_window, bg=theme["color"], fg=theme["fg"], insertbackground=theme["ct"], font=("Calibri", 14), borderwidth=5)
    _new_window.title(lang[180])
    _new_editor.pack()
    _new_button = Button(_new_window, text=lang[181], command=lambda:
        clear_log_screen(_new_editor))
    _new_button.pack()

    with open(f"{user_data}/log.wclassic", "r", encoding="utf-8") as _TEMP_LOG:
        temp_log = _TEMP_LOG.read()
        _new_editor.insert(0.0, str(temp_log))
        _TEMP_LOG.close()

    _LOG.write(f"{str(now)} - The Log File has been shown: OK\n")


class SignaturePlugin:
    @staticmethod
    def custom():
        with open(f"{config}/signature.wclassic", "r", encoding="utf-8") as SIGNATURE_FILE:
            signature = SIGNATURE_FILE.read()
            SIGNATURE_FILE.close()

        TextWidget.insert(END, f"\n\n{str(signature)}")

        _LOG.write(f"{str(now)} - The Custom signature has been inserted: OK\n")

    @staticmethod
    def getx() -> str:
        with open(f"{config}/signature.wclassic", "r", encoding="utf-8") as SIGNATURE_FILE:
            signature = SIGNATURE_FILE.read()
            SIGNATURE_FILE.close()
            
        return signature

    @staticmethod
    def auto():
        username = getuser()
        transformed_username = username.title()

        signature = f"--\n{lang[132]}\n{transformed_username}"

        TextWidget.insert(END, f"\n\n{str(signature)}")

        _LOG.write(f"{str(now)} - The Auto signature has been inserted: OK\n")

def commandPrompt():
    askNow = sdg.askstring(lang[68], lang[69])

    if askNow == 'open' or askNow == 'openfile':
        OpenFile(desktop_win)

    elif askNow == 'about':
        aboutApp()

    elif askNow == "newfile":
        newFile()

    elif askNow == 'help':
        APP_HELP()

    elif askNow == 'fun' or askNow == 'egg':
        surprise_egg()

    elif askNow == 'data':
        appCredits()

    elif askNow == 'exit' or askNow == 'quit':
        QUIT_WRITER(desktop_win)

    elif askNow == 'clear':
        WipeFile(desktop_win)

    elif askNow == 'save as':
        SaveFile(desktop_win)

    elif askNow == 'save':
        Save(desktop_win)

    elif askNow == 'clock open':
        clockPlugin()

    elif askNow == 'font family':
        fontEdit(2)

    elif askNow == 'font size':
        fontEdit(1)

    elif askNow == 'ragequit':
        quickway()

    elif askNow == 'repo':
        repo()

    elif askNow == 'notes':
        new_window()

    elif askNow == 'win size':
        SetWinSize()

    elif askNow == '':
        pass

    else:
        mb.showerror(lang[68], lang[70])

# Key bindings
desktop_win.bind('<Control-o>', lambda b:
    OpenFile(desktop_win))

desktop_win.bind('<Control-s>', lambda c:
    Save(desktop_win))

desktop_win.bind('<Control-z>', lambda c:
    SaveFile(desktop_win))

desktop_win.bind('<Control-a>', lambda e:
    aboutApp())

desktop_win.bind('<Control-h>', lambda f:
    APP_HELP())

desktop_win.bind('<Control-d>', lambda g:
    ThemeSet('black', 'white', 'white', 'dark grey', 'black'))

desktop_win.bind('<Control-l>', lambda h:
    ThemeSet('white', 'black', 'black', 'black', 'white'))

desktop_win.bind('<Control-g>', lambda j:
    SetWinSize())

desktop_win.bind('<Control-r>', lambda l:
    clockPlugin())

desktop_win.bind('<Control-w>', lambda m:
    commandPrompt())


def on_closing():
    result = mb.askyesno(lang[53], lang[54])

    if result == False:
        return

    desktop_win.destroy()

def QUIT_WRITER(*args, **kargs):
    """
    QUIT_WRITER quits the software using on_closing
    """

    on_closing()

# Creating the menu dropdowns and buttons
menu_10.add_command(label=lang[94], command=newFile)
menu_10.add_command(label=lang[7], command=lambda:
    OpenFile(desktop_win))
menu_10.add_separator()
menu_10.add_command(label = lang[8], command=lambda:
    Save(desktop_win))
menu_10.add_command(label = lang[9], command=lambda:
    SaveFile(desktop_win))
menu_10.add_separator()
menu_10.add_command(label=lang[163], command=DOC_STATS)
menu_10.add_separator()
menu_10.add_command(label=lang[11], command=lambda:
    QUIT_WRITER(desktop_win))


if startApp == "1":
    menu_11.add_command(label=lang[75], command=UpdateCheck.check)
    menu_11.add_separator()
menu_11.add_command(label=lang[25], command=aboutApp)
menu_11.add_command(label=lang[186], command=lambda:
    simple_webbrowser.Website("https://www.buymeacoffee.com/mf366"))
menu_11.add_command(label=lang[26], command=APP_HELP)
menu_11.add_command(label=lang[27], command=repo)
menu_11.add_command(label=lang[179], command=show_log)
menu_11.add_separator()
menu_11.add_command(label=lang[28], command=appCredits)
menu_11.add_separator()
menu_11.add_command(label=lang[137], command=Tips_Tricks)
menu_11.add_separator()
menu_11.add_command(label=lang[29], command=surprise_egg)

menu_1.add_command(label=lang[12], command=SetWinSize)


menu_7.add_command(label=lang[20], command=lambda:
                        fontEdit(1))
menu_7.add_command(label=lang[21], command=lambda:
                        fontEdit(2))


menu_8.add_command(label=lang[22], command=new_window)
menu_8.add_command(label=lang[23], command=clockPlugin)
menu_8.add_command(label=lang[182], command=Terminal)
menu_8.add_separator()
menu_8.add_command(label=lang[131], command=SignaturePlugin.custom)
menu_8.add_command(label=lang[130], command=SignaturePlugin.auto)
menu_8.add_separator()
menu_8.add_command(label=lang[10], command=lambda:
    WipeFile(desktop_win))
menu_8.add_separator()
menu_8.add_command(label=lang[173], command=lambda:
    PluginCentral(window=Toplevel(desktop_win)))

menu_9.add_command(label=lang[81], command=InternetOnWriter.Website)
menu_9.add_separator()
menu_9.add_command(label=lang[87], command=lambda:
    InternetOnWriter.Search('google'))
menu_9.add_command(label=lang[86], command=lambda:
    InternetOnWriter.Search('bing'))
menu_9.add_command(label=lang[89], command=lambda:
    InternetOnWriter.Search('ysearch'))
menu_9.add_command(label=lang[88], command=lambda:
    InternetOnWriter.Search('ddgo'))
menu_9.add_command(label=lang[138], command=lambda:
    InternetOnWriter.Search("brave"))
menu_9.add_command(label=lang[95], command=lambda:
    InternetOnWriter.Search("ecosia"))
menu_9.add_command(label=lang[106], command=lambda:
    InternetOnWriter.Search("qwant"))
menu_9.add_separator()
menu_9.add_command(label=lang[97], command=lambda:
    InternetOnWriter.Search("stack"))
menu_9.add_separator()
menu_9.add_command(label=lang[96], command=lambda:
    InternetOnWriter.Search("yt"))
menu_9.add_command(label=lang[103], command=lambda:
    InternetOnWriter.Search("soundcloud"))
menu_9.add_command(label=lang[125], command=lambda:
    InternetOnWriter.Search("spotify"))
menu_9.add_separator()
menu_9.add_command(label=lang[107], command=lambda:
    InternetOnWriter.Search("archive"))
menu_9.add_separator()
menu_9.add_command(label=lang[169], command=lambda:
    InternetOnWriter.Search("github"))
menu_9.add_command(label=lang[171], command=lambda:
    InternetOnWriter.Search("gitlab"))

menu_13.add_command(label="Čeština (Čechie)", command=lambda:
    LanguageSet("cs", desktop_win))
menu_13.add_command(label="Dansk (Danmark)", command=lambda:
    LanguageSet("da", desktop_win))
menu_13.add_command(label="Deutsch (Deutschland)", command=lambda:
    LanguageSet("de", desktop_win))
menu_13.add_command(label='English (America)', command=lambda:
    LanguageSet('en', desktop_win))
menu_13.add_command(label='Español (España)', command=lambda:
    LanguageSet('es', desktop_win))
menu_13.add_command(label='Français (France)', command=lambda:
    LanguageSet('fr', desktop_win))
menu_13.add_command(label='Italiano (Italia)', command=lambda:
    LanguageSet('it', desktop_win))
menu_13.add_command(label='Ελληνικά (Ελλάδα)', command=lambda:
    LanguageSet("el", desktop_win))
menu_13.add_command(label="Norsk (Norge)", command=lambda:
    LanguageSet("nb", desktop_win))
menu_13.add_command(label='Português (Brasil)', command=lambda:
    LanguageSet('br', desktop_win))
menu_13.add_command(label='Português (Portugal)', command=lambda:
    LanguageSet('pt', desktop_win))
menu_13.add_command(label='Slovenčina (Slovensko)', command=lambda:
    LanguageSet('sk', desktop_win))
menu_13.add_command(label="Svenska (Sverige)", command=lambda:
    LanguageSet("sv", desktop_win))
menu_13.add_command(label="Українська (Україна)", command=lambda:
    LanguageSet("uk", desktop_win))

menu_12.add_cascade(label=lang[198], menu=menu_13)
menu_12.add_separator()
menu_12.add_command(label=lang[74], command=UpdateCheck.change)
menu_12.add_separator()

if sys.platform == "linux":
    menu_12.add_command(label=lang[192], command=desktop_create_win)
    menu_12.add_separator()

menu_12.add_command(label=lang[190], command=lambda:
    lock_a_win(desktop_win, True))
menu_12.add_command(label=lang[191], command=lambda:
    lock_a_win(desktop_win, False))
menu_12.add_separator()
menu_12.add_command(label=lang[76], command=lambda:
    resetWriter(desktop_win))
menu_12.add_separator()
menu_12.add_command(label=lang[105], command=article_md)


menu_5.add_command(label=lang[16], command=lambda:
    ThemeSet('white', 'black', 'black', 'black', 'white'))
menu_5.add_command(label=lang[17], command=lambda:
    ThemeSet('black', 'white', 'white', 'white', 'black'))
menu_5.add_separator()
menu_5.add_command(label=lang[18], command=lambda:
    ThemeSet('grey', 'black', 'black', 'black', 'white'))


menu_6.add_command(label="Official WriterClassic v8.1.1+ Theme by Norb", command=lambda:
    ThemeSet("#0055FF", "#B3BFFF", "#fcfff7", "#fcfff7", "#0055FF"))

menu_6.add_separator()

menu_6.add_command(label='Light Yellow', command=lambda:
    ThemeSet('light yellow', 'black', 'black', '#f5b949', 'black'))

menu_6.add_command(label='Magic', command=lambda:
    ThemeSet('purple', 'white', 'white', '#290340', 'white'))

menu_6.add_command(label='Through the Sky', command=lambda:
    ThemeSet('light blue', 'black', 'black', '#031882', 'white'))

menu_6.add_command(label='Codetime', command=lambda:
    ThemeSet('black', 'green', 'green', 'black', 'light green'))

menu_6.add_command(label='Darkest Night Ever', command=lambda:
    ThemeSet('#040114', '#e8a78e', '#e8a78e', 'black', '#e8a78e'))

menu_6.add_command(label='Dark Forest', command=lambda:
    ThemeSet('#0e2414', '#c0db7b', '#c0db7b', '#040d07', '#ccf0c5'))

menu_6.add_command(label='Christmas Night', command=lambda:
    ThemeSet('#020421', '#a5a9e8', '#a5a9e8', '#020312', '#cbcef2'))

menu_6.add_command(label='Silent Night', command=lambda:
    ThemeSet('#020421','pink', 'pink', '#020312', '#ebd1ed'))

menu_6.add_command(label="Penguins", command=lambda:
    ThemeSet('#b8d8e0', '#bd5200', 'black', '#ffc738', 'black'))

if sys.platform == "win32":
    menu_6.add_command(label='[EXTRA] PowerShell Theme', command=lambda:
        ThemeSet("#012456", "#eeedf0", "#fedba9", "#eeedf0", "#012456"))

def adv_change():
    if settings["advanced-mode"]:
        settings["advanced-mode"] = False

    else:
        settings["advanced-mode"] = True

    ic(settings["advanced-mode"])
    fast_dump()

    mb.showinfo(message=lang[63], title=lang[1])

menu_12.add_separator()
menu_12.add_command(label="Enable/disable Advanced Mode [English]", command=adv_change)

def show_debug():
    if settings["debugging"]:
        settings["debugging"] = False

    else:
        settings["debugging"] = True

    ic(settings["debugging"])
    fast_dump()

    mb.showinfo(message=lang[63], title=lang[1])

def dencrypt():
    def runx(pathx: str, parameters: str):
        settings["dencrypt"] = pathx
        fast_dump()

        if not NOW_FILE:
            mb.showinfo(lang[1], "The file must be saved.")

        else:
            os.system(f'"{pathx}" "{NOW_FILE}" {parameters}')
            mb.showinfo(lang[1], "You need to reopen the file to see the changes unless you used the '-o' flag.")

    new = Toplevel(desktop_win)
    if sys.platform == "win32":
        new.iconbitmap(f"{data_dir}/app_icon.ico")
    new.title("WriterClassic - Use d3NCRYP7")
    new.resizable(False, False)

    label_1 = Label(new, text="d3NCRYP7 Path: ", font=("Segoe UI", 13))
    entry_1 = Entry(new, font=('Segoe UI', 13), width=58)
    label_2 = Label(new, text="Extra Flags: ", font=("Segoe UI", 13))
    entry_2 = Entry(new, font=('Segoe UI', 13), width=58)

    entry_1.insert(0, settings["dencrypt"])
    entry_2.insert(0, "-e")

    butt_1 = Button(new, text="Run!", command=lambda:
        runx(entry_1.get(), entry_2.get()))
    butt_2 = Button(new, text="What's d3NCRYP7 by MF366?", command=lambda:
        simple_webbrowser.Website("https://github.com/MF366-Coding/d3NCRYP7#d3ncryp7---simple-encryption-and-decryption-system"))

    label_1.grid(column=1, row=1)
    entry_1.grid(column=2, row=1)
    label_2.grid(column=1, row=2)
    entry_2.grid(column=2, row=2)
    butt_1.grid(column=1, row=3)
    butt_2.grid(column=2, row=3)

    new.mainloop()

def readme_gen(*entries):
    _title = entries[0]
    _describe = entries[1]
    _author_email = entries[2]
    _author_website = entries[3]
    _project_website = entries[4]
    _sponsor_site = entries[5]

    TextWidget.delete(0.0, END)

    if _title in NOT_ALLOWED:
        _title = 'Insert title here'

    if _describe in NOT_ALLOWED:
        _describe = f"Please describe {_title}"

    readme_generated = f'''# {_title}
**{_describe}**

'''

    if _author_email not in NOT_ALLOWED:
        readme_generated += f"""[Contact Me]({_author_email})\n"""

    if _author_website not in NOT_ALLOWED:
        readme_generated += f"""[I'm online at: {_author_website}]({_author_website})\n"""

    if _project_website not in NOT_ALLOWED:
        readme_generated += f"""[Find this project at: {_project_website}]({_project_website})\n"""

    if _sponsor_site not in NOT_ALLOWED:
        readme_generated += f"""[Liked it? Sponsor it!]({_sponsor_site})\n"""

    TextWidget.insert(chars=readme_generated, index=0.0)

def readme_gen_win():
    # Window Creation
    window = Toplevel(desktop_win)
    window.title("README.md Generator")
    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text='Title:', font=('Calibri', 13))
    label_2 = Label(window, text='Short Description:', font=('Calibri', 13))
    label_3 = Label(window, text='Author Email:', font=('Calibri', 13))
    label_4 = Label(window, text='Author Website:', font=('Calibri', 13))
    label_5 = Label(window, text='Project Website:', font=('Calibri', 13))
    label_6 = Label(window, text='Sponsor/Donation Website:', font=('Calibri', 13))
    label_7 = Label(window, text="NOTE:", font=("Calibri", 13))
    label_8 = Label(window, text="This action will erase the current text in the editor.", font=("Calibri", 13))

    _title = Entry(window, font=('Calibri', 12))
    _describe = Entry(window, font=('Calibri', 12))
    _author_email = Entry(window, font=('Calibri', 12))
    _author_website = Entry(window, font=('Calibri', 12))
    _project_website = Entry(window, font=('Calibri', 12))
    _sponsor_site = Entry(window, font=('Calibri', 12))

    butt_1 = Button(window, text="Generate", command=lambda:
        readme_gen(_title.get(), _describe.get(), _author_email.get(), _author_website.get(), _project_website.get(), _sponsor_site.get()))

    butt_2 = Button(window, text="Cancel", command=window.destroy)

    label_1.grid(column=1, row=2)
    label_2.grid(column=1, row=3)
    label_3.grid(column=1, row=4)
    label_4.grid(column=1, row=5)
    label_5.grid(column=1, row=6)
    label_6.grid(column=1, row=7)
    label_7.grid(column=1, row=1)
    label_8.grid(column=2, row=1)

    _title.grid(column=2, row=2)
    _describe.grid(column=2, row=3)
    _author_email.grid(column=2, row=4)
    _author_website.grid(column=2, row=5)
    _project_website.grid(column=2, row=6)
    _sponsor_site.grid(column=2, row=7)

    butt_1.grid(column=1, row=8)
    butt_2.grid(column=2, row=8)

    window.mainloop()

def open_with_adv():
    window = Toplevel(desktop_win)
    window.title("Open With...")
    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    def action_1():
        if not NOW_FILE:
            mb.showinfo(lang[1], "The file must be saved.")
        else:
            os.system(f'"{str(NOW_FILE)}"')

        window.destroy()

    def action_2(requested_entry):
        if not NOW_FILE:
            mb.showinfo(lang[1], "The file must be saved.")
        else:
            if " " in requested_entry:
                os.system(f'"{requested_entry}" "{str(NOW_FILE)}"')
            else:
                os.system(f'{requested_entry} "{str(NOW_FILE)}"')

        window.destroy()

    butt_1 = Button(window, text="Use the default app", command=action_1)
    label_1 = Label(window, text="...or...".upper(), font=("Arial", 15))
    label_2 = Label(window, text="Custom Path:", font=("Calibri", 13))
    entry_1 = Entry(window, font=("Calibri", 13))
    butt_2 = Button(window, text="Open with the app at...", command=lambda:
        action_2(entry_1.get()))

    butt_1.grid(column=1, row=1)
    label_1.grid(column=1, row=2)
    label_2.grid(column=1, row=3)
    entry_1.grid(column=2, row=3)
    butt_2.grid(column=1, row=4)

    window.mainloop()

def send_email_with_attachment(win, signa: bool, sender_email: str, sender_password: str, recipient_email: str, subject: str, body: str):
    win.destroy()
    
    if not signa:
        body += "\n\nSent with WriterClassic (https://mf366-coding.github.io/writerclassic.html)"
    
    elif signa:
        body += f"\n\n{SignaturePlugin.getx()}"

    # Certain parts of this function belongs to:
    # https://medium.com/@hannanmentor/20-python-scripts-with-code-to-automate-your-work-68662a8dcbc1
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with open(NOW_FILE, "r", encoding="utf-8") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(NOW_FILE)}")
            message.attach(part)
        server.sendmail(sender_email, recipient_email, message.as_string())
    
    except Exception:
        mb.showerror(lang[1], "A fatal error ocurred.\nThe already cached emails will probably be sent but the rest won't.")

    server.quit()

def message_write(mail: str, pwd: str, _variable, win):
    win.destroy()
    
    if _variable == '1':
        try:
            settings["email"] = str(mail)
            fast_dump()
        except Exception:
            pass
    
    # Window Creation
    window = Toplevel(desktop_win)
    window.title("WriterClassic - Write the email")
    
    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')
        
    label_1 = Label(window, text="Send to: ", font=("Noto Sans", 13))
    label_2 = Label(window, text="Only one email allowed.", font=("Noto Sans", 11))
    label_3 = Label(window, text="Subject: ", font=("Noto Sans", 13))
    label_4 = Label(window, text="Message: ", font=("Noto Sans", 13))
    
    entry_1 = Entry(window, font=("Noto Sans", 13))
    entry_2 = Entry(window, font=("Noto Sans", 13))
    
    text_1 = Text(window, borderwidth=5, font=(font_use["type"], font_use["size"]), insertbackground=theme["ct"], fg=theme["fg"], bg=theme["color"], height=10)
    
    butt_1 = Button(window, text="Send", command=lambda:
        send_email_with_attachment(window, False, mail, pwd, entry_2.get(), entry_1.get(), text_1.get(0.0, END)))
    
    butt_2 = Button(window, text="Send using your Custom Signature", command=lambda:
        send_email_with_attachment(window, True, mail, pwd, entry_2.get(), entry_1.get(), text_1.get(0.0, END)))
    
    label_1.pack()
    label_2.pack()
    entry_2.pack()
    
    label_3.pack()
    entry_1.pack()
    
    label_4.pack()
    text_1.pack()
    
    butt_1.pack()
    butt_2.pack()
    
    window.mainloop()
    

def adv_login():
    # Window Creation
    if not NOW_FILE:
        mb.showerror(lang[1], "The file must be saved.")
        return
    
    window = Toplevel(desktop_win)
    window.title("WriterClassic - Login with your Personal Outlook account")
    
    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')
        
    label_1 = Label(window, text="Login with your Personal Outlook account", font=("Noto Sans", 14))
    label_2 = Label(window, text="WriterClassic has no affiliation with Microsoft in any way. Please note that!", font=("Noto Sans", 11))
    label_3 = Label(window, text="We will NEVER save your password. We respect your security and privacy.", font=("Noto Sans", 12))
    label_4 = Label(window, text="Email: ", font=("Noto Sans", 13))
    label_5 = Label(window, text="Password: ", font=("Noto Sans", 13))
    
    entry_1 = Entry(window, font=("Noto Sans", 12))
    entry_2 = Entry(window, font=("Noto Sans", 10))
    
    entry_1.insert(0, settings["email"])
    
    a = StringVar(window)
    
    butt_1 = Checkbutton(window, text="Save my email for future use", variable=a)
    butt_2 = Button(window, text="Login", command=lambda:
        message_write(entry_1.get(), entry_2.get(), a.get(), window))
    
    label_1.pack()
    label_2.pack()
    label_3.pack()
    label_4.pack()
    entry_1.pack()
    label_5.pack()
    entry_2.pack()
    butt_1.pack()
    butt_2.pack()
    
    window.mainloop()

def show_advV():
    mb.showinfo(lang[1], f"You are running WriterClassic {advV}.")

if ADVANCED:
    menu_14.add_command(label="Show/hide debugging sentences (Not recommended)", command=show_debug)
    if sys.platform == "win32":
        menu_14.add_command(label="Encrypt/decrypt current file with d3NCRYP7", command=dencrypt)
    menu_14.add_command(label="README.md Generator", command=readme_gen_win)
    menu_14.add_command(label="Open with...", command=open_with_adv)
    menu_14.add_command(label="Send file via email", command=adv_login)
    menu_14.add_command(label="Advanced Versioning", command=show_advV)

try:
    if sys.platform == "linux":
        # Themed menus in case of: Linux Python3
        menu_10.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_11.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_1.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_2.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_3.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_5.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_4.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_6.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_7.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_12.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_8.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_9.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_13.configure(background=theme["menu"], foreground=theme["mfg"])
        _LOG.write(f"{str(now)} - The Menus have been themed [LINUX ONLY]: OK\n")
except TclError:
    if sys.platform == "linux":
        # Themed menus in case of: Linux Python3
        mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_10.configure(background="white", foreground="black")
        menu_11.configure(background="white", foreground="black")
        menu_1.configure(background="white", foreground="black")
        menu_2.configure(background="white", foreground="black")
        menu_3.configure(background="white", foreground="black")
        menu_5.configure(background="white", foreground="black")
        menu_4.configure(background="white", foreground="black")
        menu_6.configure(background="white", foreground="black")
        menu_7.configure(background="white", foreground="black")
        menu_12.configure(background="white", foreground="black")
        menu_8.configure(background="white", foreground="black")
        menu_9.configure(background="white", foreground="black")
        menu_13.configure(background="white", foreground="black")
        _LOG.write(f"{str(now)} - The Menus have been themed [LINUX ONLY]: OK\n")

# dropdowns/cascades
menu_bar.add_cascade(label=lang[2],menu=menu_10)
menu_bar.add_cascade(label=lang[3],menu=menu_1)
menu_1.add_cascade(label=lang[13], menu=menu_4)
menu_4.add_cascade(label=lang[15], menu=menu_5)
menu_4.add_cascade(label=lang[19], menu=menu_6)
menu_4.add_separator()
menu_4.add_command(label=lang[153], command=lambda:
    simple_webbrowser.Website(url="https://github.com/MF366-Coding/WriterClassic-ExtraThemes"))
menu_1.add_cascade(label=lang[14], menu=menu_7)
menu_bar.add_cascade(label=lang[4], menu=menu_8)
menu_bar.add_cascade(label=lang[79], menu=menu_9)
menu_bar.add_cascade(label=lang[5], menu=menu_12)
menu_bar.add_cascade(label=lang[6], menu=menu_11)

if ADVANCED:
    menu_bar.add_cascade(label="Advanced Mode [English]", menu=menu_14)

# Yes, menu_bar is desktop_win's menu bar lmfao
desktop_win.configure(menu=menu_bar)
_LOG.write(f"{str(now)} - The Menu bar has been configured correctly: OK\n")

if len(sys.argv) > 1:
    # The first command-line argument is the file path
    file_path = sys.argv[1]

    try:
        file_input = open(file_path, "rt", encoding="utf-8")
        file_data = file_input.read()

        desktop_win.title(f"WriterClassic - {file_path}")
        TextWidget.delete(index1=0.0, index2=END)
        TextWidget.insert(chars=file_data, index=0.0)

        NOW_FILE = str(file_path)
        file_input.close()
        _LOG.write(f"{str(now)} - A file at the path {str(file_path)} has been opened: OK\n")

    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
        mb.showerror(title=lang[187], message=f"{lang[188]} {str(file_path)}.")
        run_default = mb.askyesno(title=lang[187], message=lang[189])
        if run_default:
            os.system(str(file_path))

    except FileNotFoundError as e:
        desktop_win.destroy()
        print(e)
        quit()

    finally:
        ic(NOW_FILE)

desktop_win.protocol("WM_DELETE_WINDOW", on_closing)

# And done! Now, it will continuously mainlooping! Enjoy!
desktop_win.mainloop()
