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

Original idea by: MF366
Fully developed by: MF366

Small but lovely contributions by:
    Norb (norbcodes at GitHub)
    Zeca70 (Zeca70 at GitHub)
'''

NOW_FILE = False

print(NOW_FILE)

import sys # Platforms and OSes
import random
import os
import datetime # Really, bro?
import json # google it lmfao

now = datetime.datetime.now()

_LOG = open("log.txt", mode="a", encoding="utf-8")

_LOG.write("\n")
_LOG.write(f"{str(now)} - WriterClassic was executed: OK\n")

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

with open('config/startup.txt', 'r', encoding='utf-8') as startupFile:
    startAppData = startupFile.read()
    startApp = startAppData[0:1]
    if startApp == "0":
        startApp = "0"
        _LOG.write(f"{str(now)} - Check for updates on startup: DISABLED\n")
        
    elif startApp == "1":
        startApp = "1"
        _LOG.write(f"{str(now)} - Check for updates on startup: ENABLED\n")
        
    else:
        startApp = "1"
        _LOG.write(f"{str(now)} - Check for updates on startup: ENABLED\n")
        

# Importing the goodies
from py_compile import compile as _compile
_LOG.write(f"{str(now)} - Imported compile from py_compile: OK\n")

from getpass import getuser
_LOG.write(f"{str(now)} - Imported getuser from getpass: OK\n")

try:
    from tkinter import * # Window
    _LOG.write(f"{str(now)} - Imported tkinter: OK\n")
except ModuleNotFoundError:
    _LOG.write(f"{str(now)} - Imported tkinter: ERROR\n")
    from Tkinter import *
    _LOG.write(f"{str(now)} - Attempted to import Tkinter from Python 2: OK\n")

try:
    from tkinter.ttk import * # Not sure
    _LOG.write(f"{str(now)} - Imported tkinter.ttk: OK\n")
    from tkinter import simpledialog as sdg # Inputs with GUI
    _LOG.write(f"{str(now)} - Imported simpledialog from tkinter: OK\n")
    import tkinter.filedialog as dlg # File Dialogs were never this easy...
    _LOG.write(f"{str(now)} - Imported filedialog from tkinter: OK\n")
    import tkinter.messagebox as mb # Never gonna give you up... (Pop-ups)
    _LOG.write(f"{str(now)} - Imported messagebox from tkinter: OK\n")
    from tkinter.font import Font # Ouchie mama (font, daaah)
    _LOG.write(f"{str(now)} - Imported Font from tkinter.font: OK\n")
except ModuleNotFoundError:
    _LOG.write(f"{str(now)} - Imported tkinter.ttk: ERROR\n")
    from Tkinter.ttk import *
    _LOG.write(f"{str(now)} - Attempted to import Tkinter.ttk: OK\n")
    
    _LOG.write(f"{str(now)} - Imported simpledialog from tkinter: ERROR\n")
    from Tkinter import simpledialog as sdg
    _LOG.write(f"{str(now)} - Attempted to import simpledialog from Tkinter: OK\n")
    
    _LOG.write(f"{str(now)} - Imported filedialog from tkinter: ERROR\n")
    import Tkinter.filedialog as dlg # File Dialogs were never this easy...
    _LOG.write(f"{str(now)} - Attempted to import filedialog from Tkinter: OK\n")
    
    _LOG.write(f"{str(now)} - Imported messagebox from tkinter: ERROR\n")
    import Tkinter.messagebox as mb # Never gonna give you up... (Pop-ups)
    _LOG.write(f"{str(now)} - Attempted to import filedialog from Tkinter: OK\n")
    
    _LOG.write(f"{str(now)} - Imported Font from tkinter.font: ERROR\n")
    from Tkinter.font import Font # Ouchie mama (font, daaah)
    _LOG.write(f"{str(now)} - Attempted to import Font from Tkinter.font: OK\n")

with open('config/lang.txt', 'r', encoding="utf-8") as configLangFile:
    setLang = configLangFile.read()
    _LOG.write(f"{str(now)} - Language ({str(setLang[0:2])}): ENABLED\n")

with open('data/'+str(setLang[0:2])+'.txt', 'r', encoding='utf-8') as usedLangFile:
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
        import requests # it's a module yay!
        _LOG.write(f"{str(now)} - requests has been imported: OK\n")
    except (ModuleNotFoundError, ImportError):
        _LOG.write(f"{str(now)} - requests has been imported: ERROR\n")
        mb.showerror(lang[155], lang[156])
        module_pip = mb.askyesno(lang[155], lang[157])
        if module_pip:
            if sys.platform == "win32":
                os.system("python -m pip install requests")
                mb.showinfo(lang[155], lang[158])
                _LOG.write(f"{str(now)} - Command 'pip install simple_webbrowser' has been executed: OK\n")
                _LOG.write(f"{str(now)} - End of session\n")
                quit()
            elif sys.platform in UNIX_OSES:
                os.system("pip install requests")
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

try:
    from data import plugins as plugin
    _LOG.write(f"{str(now)} - WriterClassic's plugins have been imported: OK\n")
except (ModuleNotFoundError, ImportError):
    _LOG.write(f"{str(now)} - [WARNING!] WriterClassic's plugins have been imported: ERROR (FILE DAMAGED OR FILE DOES NOT EXIST)\n")
    mb.showerror(lang[161], f"{lang[162]}\n{lang[160]}")
    quit()

# Windowing
desktop_win = Tk()
_LOG.write(f"{str(now)} - WriterClassic launched: OK\n")

if sys.platform == "win32":
    desktop_win.iconbitmap("data/app_icon.ico")
    _LOG.write(f"{str(now)} - Icon has been changed to WriterClassic's icon [WINDOWS ONLY]: OK\n")

latest_version = None

IGNORE_CHECKING = False

if startApp == '1':
    try:
        response = requests.get('https://api.github.com/repos/MF366-Coding/WriterClassic/releases/latest', timeout=3.5)
        _LOG.write(f"{str(now)} - Connected to GitHub: OK\n")
        data = json.loads(response.text)
        _LOG.write(f"{str(now)} - Got WriterClassic Releases data: OK\n")
        latest_version = data['tag_name']
        _LOG.write(f"{str(now)} - Got the latest release's tag: OK\n")
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.ReadTimeout):
        mb.showerror(lang[148], f"{lang[135]}\n{lang[136]}")
        _LOG.write(f"{str(now)} - Connected to GitHub: ERROR\n")
        _LOG.write(f"{str(now)} - Connection has timed out, is restricted or is simply unavailable: INFO\n")
        IGNORE_CHECKING = True
        _LOG.write(f"{str(now)} - WriterClassic is launching without checking for updates: OK\n")

# Config files
with open('data/version.txt', 'r', encoding='utf-8') as versionFile:
    appVGet = versionFile.read()
    appV = appVGet[0:6]
    _LOG.write(f"{str(now)} - Got the current version: OK\n")
    #print(appV)

with open('config/theme.json', 'rt', encoding='utf-8') as textColor:
    theme = json.load(textColor)
    _LOG.write(f"{str(now)} - Got the current theme: OK\n")

with open('config/font.json', 'rt', encoding='utf-8') as fontFile:
    font_use = json.load(fontFile)
    _LOG.write(f"{str(now)} - Got the current font family/type: OK\n")
    _LOG.write(f"{str(now)} - Got the current font size: OK\n")
    fontFile.close()

# Windowing... again
desktop_win.title(lang[1])
_LOG.write(f"{str(now)} - Window's title was set to WriterClassic: OK\n")
try:
    FontSet = Font(family=font_use["font-type"], size=font_use["font-size"])
    __font_type = font_use["font-type"]
    __font_size = font_use["font-size"]
    _LOG.write(f"{str(now)} - Font size is {str(__font_size)}: OK\n")
    _LOG.write(f"{str(now)} - Font family/type is {str(__font_type)}: OK\n")
except TclError:
    mb.showerror(lang[149], f"{lang[144]}\n{lang[145]}\n{lang[146]}")
    _LOG.write(f"{str(now)} - Font size is set to 14 because of a font error: OK\n")
    FontSet = Font(family="Segoe UI", size=14)
    _LOG.write(f"{str(now)} - Font type is set to Segoe UI because of a font error: OK\n")
    with open('config/font.json', 'w', encoding='utf-8') as fixed_fontFile:
        new_font = {
            "font-type":"Segoe UI",
            "font-size":14
        }
        json.dump(new_font, fixed_fontFile)
        _LOG.write(f"{str(now)} - The themes were reconfigured because of a font error: OK\n")

TextWidget = Text(desktop_win, font=FontSet)
_LOG.write(f"{str(now)} - The editing interface has been created: OK\n")

with open('config/geom.txt', 'r', encoding='utf-8') as geom_bg:
    geomValue = geom_bg.read()
    _LOG.write(f"{str(now)} - Got the window's dimensions settings: OK\n")

GeomValues = geomValue.split('x')

desktop_win.geometry(geomValue)

try:
    TextWidget.configure(bg=theme["color"], fg=theme["fg"], width=GeomValues[0], height=GeomValues[1], insertbackground=theme["ct"])
except TclError:
    mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
    TextWidget.configure(bg="black", fg="white", width=GeomValues[0], height=GeomValues[1], insertbackground="white")

TextWidget.pack()

# Closing the configs
geom_bg.close()
configLangFile.close()

# Defining the menu bar
menu_bar = Menu(desktop_win)

try:
    if sys.platform == "linux":
        menu_bar.configure(background=theme["menu"], foreground=theme["mfg"])
except TclError:
    if sys.platform == "linux":
        mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_bar.configure(background="white", foreground="black")

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
menu_13 = Menu(menu_8)

def writeStartup(text):
    with open('config/startup.txt', 'w', encoding='utf-8') as startupWriteFile:
        startupWriteFile.write(text)
        startupWriteFile.close()

# Check for Updates
class UpdateCheck:
    @staticmethod
    def check_other():
        if appV != latest_version and IGNORE_CHECKING == False:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')
        elif IGNORE_CHECKING == True:
            pass

    @staticmethod
    def check():
        if appV != latest_version and IGNORE_CHECKING == False:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')
        elif appV == latest_version and IGNORE_CHECKING == False:
            mb.showinfo(title=lang[93], message=lang[92])
        else:
            mb.showerror(lang[148], f"{lang[135]}\n{lang[136]}")

    @staticmethod
    def change():
        if startApp == '1':
            writeStartup('0')
            mb.showinfo(title=lang[1], message=lang[101])
        else:
            writeStartup('1')
            mb.showinfo(title=lang[1], message=lang[101])

if startApp == '1':
    UpdateCheck.check_other()

# Windowing... one more time...
def SetWinSize():
    widthSet = sdg.askinteger(lang[1], lang[57])
    if widthSet in NOT_ALLOWED:
        mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
    elif widthSet not in NOT_ALLOWED:
        heightSet = sdg.askinteger(lang[1], lang[58])
        if heightSet in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif heightSet not in NOT_ALLOWED:
            TextWidget.configure(width=widthSet, height=heightSet)
            desktop_win.geometry(str(widthSet)+'x'+str(heightSet))
            with open('config/geom.txt', 'w', encoding='utf-8') as geomdata:
                geomdata.write('')
                geomdata.write(str(widthSet)+'x'+str(heightSet))
            geomdata.close()

# Theme Picker
def ThemeSet(colour_first, colour_second, colour_third, colour_fourth, colour_fifth):
    with open('config/theme.json', 'wt') as fileColored:
        new_obj = {
            "color":str(colour_first),
            "ct":str(colour_third),
            "fg":str(colour_second),
            "mfg":str(colour_fifth),
            "menu":str(colour_fourth)
        }
        json.dump(new_obj, fileColored)

    TextWidget.configure(bg=colour_first, fg=colour_second, insertbackground=colour_third)
    TextWidget.pack()

    waitResponse = mb.askyesno(parent=desktop_win, title=lang[30], message=lang[31])
    if waitResponse:
        desktop_win.destroy()

# ragequit
def quickway():
    desktop_win.destroy()

# Setup (Lang files)
def LanguageSet(language_set, root_win):
    with open('config/lang.txt', 'w', encoding='utf-8') as deleteThat:
        deleteThat.write('')
        deleteThat.write(language_set)
    popup_define = mb.askyesno(parent=root_win, title=lang[30], message=lang[31])
    if popup_define:
        root_win.destroy()

# Notepad
def new_window():
    newWindow = Toplevel(desktop_win)

    # Windowing... yet once more LMAO...
    newWindow.title(lang[22])
    newWindow.geometry("600x400")


    TextWidget = Text(newWindow)

    TextWidget.configure(bg=theme["color"], fg=theme["fg"], width=GeomValues[0], height=GeomValues[1], insertbackground=theme["ct"], font=FontSet)
    TextWidget.pack()

    # Closing what I no longer need
    geom_bg.close()
    configLangFile.close()

    newWindow.mainloop()

# Repo
def repo():
    ourRepo = "https://github.com/MF366-Coding/WriterClassic/"

    simple_webbrowser.Website(ourRepo)

# Clock
def clockPlugin():
    clockWindow = Toplevel(desktop_win)

    #Windowing
    clockWindow.title(lang[23])

    TextWidget = Label(clockWindow)

    TextWidget.configure(text=datetime.datetime.now())
    TextWidget.configure(
        font=(100)
        )

    clockWindow.geometry('275x65')

    TextWidget.pack()
    clockWindow.mainloop()

# Text font
def fontEdit(winType):
    global font_use

    if winType == 1:
        fontSize = sdg.askinteger(lang[59], lang[60], minvalue=1)
        if fontSize in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif fontSize not in NOT_ALLOWED:
            with open('config/font.json', 'wt', encoding='utf-8') as fontFileUse:
                font_use["font-size"] = fontSize
                new_object = {
                    "font-type":font_use["font-type"],
                    "font-size":fontSize
                }
                json.dump(new_object, fontFileUse)
                fontFileUse.close()
                mb.showinfo(lang[1], lang[63])
    else:
        fontType = sdg.askstring(lang[61], lang[62])
        if fontType in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif fontType not in NOT_ALLOWED:
            with open('config/font.json', 'wt', encoding='utf-8') as fontFileUse:
                font_use["font-type"] = fontType
                new_object = {
                    "font-type":fontType,
                    "font-size":font_use["font-size"]
                }
                json.dump(new_object, fontFileUse)
                fontFileUse.close()
                mb.showinfo(lang[1], lang[63])


# clears the screen
def newFile():
    global NOW_FILE
    
    desktop_win.title(lang[1])
    TextWidget.delete(index1=0.0, index2=END)
    NOW_FILE = False
    
    print(NOW_FILE)


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

# opens a file
def OpenFile(root_win):
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

    file_input = open(file_path, "rt")
    file_data = file_input.read()

    root_win.title(f"{lang[1]} - {file_path}")
    TextWidget.delete(index1=0.0, index2=END)
    TextWidget.insert(chars=file_data, index=0.0)
    NOW_FILE = str(file_path)
    file_input.close()
    print(NOW_FILE)


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
    NOW_FILE = str(file_path)
    print(NOW_FILE)

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
        NOW_FILE = str(file_path)
        print(NOW_FILE)

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

        file_input = open(file_path, "wt")
        file_input.write('')
        mb.showinfo(title=lang[1], message=lang[101])
        root_win.title(lang[1])
        file_input.close()

# Non-raged quit
def QUIT_WRITER(root_win):
    confirm = mb.askyesno(title=lang[53], message=lang[54])
    if confirm:
        root_win.destroy()

# credits
def appCredits():
    mb.showinfo(title=lang[28], message=lang[65])

# easter egg super secret!
def surprise_egg():
    askNow = sdg.askstring(lang[29], lang[66])

    if askNow == 'Nice stuff!!':
        simple_webbrowser.Website('https://www.youtube.com/watch?v=W6FG7yVUaKQ')

    elif askNow == 'Scan':
        mb.showwarning("Your PC has virus!", "Press Alt+F4 to remove all viruses!!!\nDo it!!!")

    elif askNow == "":
        pass

    else:
        mb.showerror(lang[29], lang[67])

# help me pls!!!
def APP_HELP():
    simple_webbrowser.Website("https://github.com/MF366-Coding/WriterClassic#help")

# infoooooo
def aboutApp(thing2, thing3):
    with open(thing2, thing3, encoding='utf-8') as about_d:
        about_data = about_d.read()
    mb.showinfo(title=lang[64], message=about_data)
    about_d.close()

def Tips_Tricks():
    picked_text = random.choice((
        lang[140],
        lang[141],
        lang[142],
        lang[143]
    ))

    mb.showinfo(lang[1], picked_text)

def resetWriter(rootWin):
    askSOS = mb.askyesno(lang[77], lang[78])
    if askSOS:
        with open('config/font.json', 'wt', encoding='utf-8') as fontFileNew:
            new_values = {
                "font-type":"Noto Sans",
                "font-size":13
            }
            json.dump(new_values, fontFileNew)

        fontFileNew.close()

        LanguageSet('en', rootWin)
        ThemeSet('black', 'white', 'white', 'black', 'white')

        desktop_win.geometry('700x500')
        with open('config/geom.txt', 'w', encoding='utf-8') as geomdata:
            geomdata.write('')
            geomdata.write('700x500')
            geomdata.close()

        with open("data/signature.txt", "w", encoding='utf-8') as sigFILE:
            sigFILE.write("--\nBest regards,\nThis is a customizable signature in a file named signature.txt in data folder...")

class InternetOnWriter:
    @staticmethod
    def Website():
        askForLink = sdg.askstring(lang[80], lang[91])
        if askForLink != ' ' or askForLink != '':
            simple_webbrowser.Website(askForLink)

    @staticmethod
    def Search(engine):
        if engine == 'google':
            askForTyping = sdg.askstring(lang[83], lang[90])
            if askForTyping != '':
                simple_webbrowser.Google(askForTyping)

        elif engine == 'bing':
            askForTyping = sdg.askstring(lang[82], lang[90])
            if askForTyping != '':
                simple_webbrowser.Bing(askForTyping)

        elif engine == 'ysearch':
            # stands for Yahoo!
            askForTyping = sdg.askstring(lang[85], lang[90])
            if askForTyping != '':
                simple_webbrowser.Yahoo(askForTyping)

        elif engine == 'ddgo':
            # stands for DuckDuckGo
            askForTyping = sdg.askstring(lang[84], lang[90])
            if askForTyping != '':
                simple_webbrowser.DuckDuckGo(askForTyping)

        elif engine == "yt":
            # stands for YouTube
            askForTyping = sdg.askstring(lang[99], lang[90])
            if askForTyping != '':
                simple_webbrowser.YouTube(askForTyping)

        elif engine == "ecosia":
            askForTyping = sdg.askstring(lang[98], lang[90])
            if askForTyping != '':
                simple_webbrowser.Ecosia(askForTyping)

        elif engine == "stack":
            # stands for Stack Overflow
            askForTyping = sdg.askstring(lang[100], lang[90])
            if askForTyping != '':
                simple_webbrowser.StackOverflow(askForTyping)

        elif engine == "soundcloud":
            askForTyping = sdg.askstring(lang[104], lang[90])
            if askForTyping != '':
                simple_webbrowser.SoundCloud(askForTyping)

        elif engine == "archive":
            # stands for The Internet Archive
            askForTyping = sdg.askstring(lang[109], lang[90])
            if askForTyping != '':
                simple_webbrowser.Archive(askForTyping)

        elif engine == "qwant":
            # stands for Qwant.com
            askForTyping = sdg.askstring(lang[108], lang[90])
            if askForTyping != '':
                simple_webbrowser.Qwant(askForTyping)

        elif engine == "spotify":
            # stands for Spotify Online
            askForTyping = sdg.askstring(lang[126], lang[90])
            if askForTyping != '':
                simple_webbrowser.SpotifyOnline(askForTyping)

        elif engine == 'brave':
            # stands for Brave Search
            askForTyping = sdg.askstring(lang[139], lang[90])
            if askForTyping != '':
                simple_webbrowser.Brave(askForTyping)

def plugin_help():
    simple_webbrowser.Website("https://github.com/MF366-Coding/WriterClassic/wiki/Plugin-Setup")

def article_md():
    simple_webbrowser.Website(url='https://github.com/MF366-Coding/WriterClassic/wiki/Manual-Configuration-Setup')


class plugins:
    title_1 = plugin.title_1
    title_2 = plugin.title_2
    title_3 = plugin.title_3
    title_4 = plugin.title_4
    title_5 = plugin.title_5
    title_6 = plugin.title_6
    title_7 = plugin.title_7

    @staticmethod
    def plugin_1(tk_root, tk_text, _file):
        plugin.plugin_1(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")

    @staticmethod
    def plugin_2(tk_root, tk_text, _file):
        plugin.plugin_2(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")

    @staticmethod
    def plugin_3(tk_root, tk_text, _file):
        plugin.plugin_3(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")

    @staticmethod
    def plugin_4(tk_root, tk_text, _file):
        plugin.plugin_4(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")

    @staticmethod
    def plugin_5(tk_root, tk_text, _file):
        plugin.plugin_5(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")

    @staticmethod
    def plugin_6(tk_root, tk_text, _file):
        plugin.plugin_6(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")

    @staticmethod
    def plugin_7(tk_root, tk_text, _file):
        plugin.plugin_7(tk_root=tk_root, tk_text=tk_text, _file=_file)
        _compile("data/plugins.py")


class SignaturePlugin:
    @staticmethod
    def custom():
        with open("data/signature.txt", "r", encoding="utf-8") as SIGNATURE_FILE:
            signature = SIGNATURE_FILE.read()
            SIGNATURE_FILE.close()

        TextWidget.insert(END, f"\n\n{str(signature)}")

    @staticmethod
    def auto():
        username = getuser()
        transformed_username = username.title()

        signature = f"--\n{lang[132]}\n{transformed_username}"

        TextWidget.insert(END, f"\n\n{str(signature)}")

def commandPrompt():
    askNow = sdg.askstring(lang[68], lang[69])

    if askNow == 'open' or askNow == 'openfile':
        OpenFile(desktop_win)

    elif askNow == 'about':
        aboutApp('data/about.txt', 'r')

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
    aboutApp('data/about.txt', 'r'))

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
menu_10.add_command(label=lang[11], command=lambda:
    QUIT_WRITER(desktop_win))


if startApp == "1":
    menu_11.add_command(label=lang[75], command=UpdateCheck.check)
    menu_11.add_separator()
menu_11.add_command(label=lang[25], command=lambda:
    aboutApp('data/about.txt', 'r'))
menu_11.add_command(label=lang[26], command=APP_HELP)
menu_11.add_command(label=lang[27], command=repo)
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
menu_8.add_separator()
menu_8.add_command(label=lang[131], command=SignaturePlugin.custom)
menu_8.add_command(label=lang[130], command=SignaturePlugin.auto)
menu_8.add_separator()
menu_8.add_command(label=lang[10], command=lambda:
    WipeFile(desktop_win))
menu_8.add_separator()


menu_13.add_command(label=plugins.title_1, command=lambda:
    plugins.plugin_1(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))

menu_13.add_command(label=plugins.title_2, command=lambda:
    plugins.plugin_2(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))

menu_13.add_command(label=plugins.title_3, command=lambda:
    plugins.plugin_3(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))

menu_13.add_command(label=plugins.title_4, command=lambda:
    plugins.plugin_4(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))

menu_13.add_command(label=plugins.title_5, command=lambda:
    plugins.plugin_5(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))

menu_13.add_command(label=plugins.title_6, command=lambda:
    plugins.plugin_6(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))

menu_13.add_command(label=plugins.title_7, command=lambda:
    plugins.plugin_7(tk_root=desktop_win, tk_text=TextWidget, _file=NOW_FILE))
menu_13.add_separator()

menu_13.add_command(label=lang[129], command=plugin_help)
menu_13.add_separator()
menu_13.add_command(label=lang[154], command=lambda:
    simple_webbrowser.Website(url="https://github.com/MF366-Coding/WriterClassic-OfficialPlugins"))


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

menu_12.add_command(label="Čeština (Čechie)", command=lambda:
    LanguageSet("cs", desktop_win))
menu_12.add_command(label="Dansk (Danmark)", command=lambda:
    LanguageSet("da", desktop_win))
menu_12.add_command(label="Deutsch (Deutschland)", command=lambda:
    LanguageSet("de", desktop_win))
menu_12.add_command(label='English (America)', command=lambda:
    LanguageSet('en', desktop_win))
menu_12.add_command(label='Español (España)', command=lambda:
    LanguageSet('es', desktop_win))
menu_12.add_command(label='Français (France)', command=lambda:
    LanguageSet('fr', desktop_win))
menu_12.add_command(label='Italiano (Italia)', command=lambda:
    LanguageSet('it', desktop_win))
menu_12.add_command(label='Ελληνικά (Ελλάδα)', command=lambda:
    LanguageSet("el", desktop_win))
menu_12.add_command(label="Norsk (Norge)", command=lambda:
    LanguageSet("nb", desktop_win))
menu_12.add_command(label='Português (Brasil)', command=lambda:
    LanguageSet('br', desktop_win))
menu_12.add_command(label='Português (Portugal)', command=lambda:
    LanguageSet('pt', desktop_win))
menu_12.add_command(label='Slovenčina (Slovensko)', command=lambda:
    LanguageSet('sk', desktop_win))
menu_12.add_command(label="Svenska (Sverige)", command=lambda:
    LanguageSet("sv", desktop_win))
menu_12.add_command(label="Українська (Україна)", command=lambda:
    LanguageSet("uk", desktop_win))
menu_12.add_separator()
menu_12.add_command(label=lang[74], command=UpdateCheck.change)
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
        menu_13.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_8.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_9.configure(background=theme["menu"], foreground=theme["mfg"])
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
        menu_13.configure(background="white", foreground="black")
        menu_8.configure(background="white", foreground="black")
        menu_9.configure(background="white", foreground="black")

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
menu_8.add_cascade(label=lang[128], menu=menu_13)
menu_bar.add_cascade(label=lang[5], menu=menu_12)
menu_bar.add_cascade(label=lang[6], menu=menu_11)

# Yes, menu_bar is desktop_win's menu bar lmfao
desktop_win.configure(menu=menu_bar)

# And done! Now, it will continuously mainlooping! Enjoy!
desktop_win.mainloop()