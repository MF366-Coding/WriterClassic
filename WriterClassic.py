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

with open('config/startup.txt', 'r', encoding='utf-8') as startupFile:
    startAppData = startupFile.read()
    startApp = startAppData[0:1]

# Importing the goodies
import sys # Platforms and OSes
import simple_webbrowser.simple_webbrowser as simple_webbrowser # internet
try:
    from tkinter import * # Window
except ModuleNotFoundError:
    from Tkinter import *
    
try:
    from tkinter.ttk import * # Not sure
    from tkinter import simpledialog as sdg # Inputs with GUI
    import tkinter.filedialog as dlg # File Dialogs were never this easy...
    import tkinter.messagebox as mb # Never gonna give you up... (Pop-ups)
    from tkinter.font import Font # Ouchie mama (font, daaah)
except:
    from Tkinter.ttk import *
    from Tkinter import simpledialog as sdg
    import Tkinter.filedialog as dlg # File Dialogs were never this easy...
    import Tkinter.messagebox as mb # Never gonna give you up... (Pop-ups)
    from Tkinter.font import Font # Ouchie mama (font, daaah)

import datetime # Really, bro?
if startApp == "1":
    import requests # it's a module yay!
import json # google it lmfao
from data import plugins as plugin
from py_compile import compile

# Windowing
desktop_win = Tk()

if sys.platform == "win32":
    desktop_win.iconbitmap("data/app_icon.ico")

latest_version = None

if startApp == '1':
    response = requests.get('https://api.github.com/repos/MF366-Coding/WriterClassic/releases/latest')
    data = json.loads(response.text)
    latest_version = data['tag_name']

# Config files
with open('config/lang.txt', 'r', encoding="utf-8") as configLangFile:
    setLang = configLangFile.read()

with open('data/'+str(setLang[0:2])+'.txt', 'r', encoding='utf-8') as usedLangFile:
    usedLang = usedLangFile.read()
    lang = usedLang.split('\n')
    #print(dd)

with open('data/version.txt', 'r', encoding='utf-8') as versionFile:
    appVGet = versionFile.read()
    appV = appVGet[0:6]
    #print(appV)

with open('config/theme.json', 'rt', encoding='utf-8') as textColor:
    theme = json.load(textColor)

with open('config/font.json', 'rt', encoding='utf-8') as fontFile:
    font_use = json.load(fontFile)

# Windowing... again
desktop_win.title(lang[1])

FontSet = Font(family=font_use["font-type"], size=font_use["font-size"])

TextWidget = Text(desktop_win, font=FontSet)

with open('config/geom.txt', 'r', encoding='utf-8') as geom_bg:
    geomValue = geom_bg.read()

GeomValues = geomValue.split('x')

desktop_win.geometry(geomValue)

TextWidget.configure(bg=theme["color"], fg=theme["fg"], width=GeomValues[0], height=GeomValues[1], insertbackground=theme["ct"])
TextWidget.pack()

# Closing the configs
geom_bg.close()
configLangFile.close()

# Defining the menu bar
menu_bar = Menu(desktop_win)

if sys.platform == "linux":
    menu_bar.configure(background=theme["menu"], foreground=theme["mfg"])

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
        if appV != latest_version:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')

    @staticmethod
    def check():
        if appV != latest_version:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')
        else:
            mb.showinfo(title=lang[93], message=lang[92])

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
    heightSet = sdg.askinteger(lang[1], lang[58])
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
    desktop_win.title(lang[1])
    TextWidget.delete(index1=0.0, index2=END)


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
    file_input.close()


# Saving as
def SaveFile(root_win):
    dados = TextWidget.get(0.0, END)
    file_path = dlg.asksaveasfilename(parent=root_win, title=lang[8], confirmoverwrite=True, filetypes=file_types, defaultextension="*.*", initialfile="New File To Save")

    # Get the selected file extension
    selected_extension = None
    for ft in file_types:
        if file_path.lower().endswith(ft[1]):
            selected_extension = ft[1]
            break

    # Append the selected extension if not already included
    if selected_extension and not file_path.lower().endswith(selected_extension):
        file_path += selected_extension

    file = open(file_path, "wt")
    file.write(str(dados))
    file.close()
    mb.showinfo(lang[1], lang[101])
    root_win.title(f"{lang[1]} - {file_path}")

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
def sair(root_win):
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
        mb.showerror("Your PC has virus!", "Press Alt+F4 to remove all viruses!!!\nDo it!!!")

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

def resetWriter(rootWin):
    askSOS = mb.askyesno(lang[77], lang[78])
    if askSOS:
        with open('config/font.json', 'wt', encoding='utf-8') as fontFileNew:
            new_values = {
                "font-type":"Segoe UI",
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
    def plugin_1(tk_root, tk_text):
        plugin.plugin_1(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")
    
    @staticmethod
    def plugin_2(tk_root, tk_text):
        plugin.plugin_2(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")
        
    @staticmethod
    def plugin_3(tk_root, tk_text):
        plugin.plugin_3(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")
        
    @staticmethod
    def plugin_4(tk_root, tk_text):
        plugin.plugin_4(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")
    
    @staticmethod
    def plugin_5(tk_root, tk_text):
        plugin.plugin_5(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")
    
    @staticmethod
    def plugin_6(tk_root, tk_text):
        plugin.plugin_6(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")
        
    @staticmethod
    def plugin_7(tk_root, tk_text):
        plugin.plugin_7(tk_root=tk_root, tk_text=tk_text)
        compile("data/plugins.py")


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
        sair(desktop_win)

    elif askNow == 'clear':
        WipeFile(desktop_win)

    elif askNow == 'save':
        SaveFile(desktop_win)

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

    else:
        mb.showerror(lang[68], lang[70])

# Key bindings

desktop_win.bind('<Control-o>', lambda b:
    OpenFile(desktop_win))

desktop_win.bind('<Control-s>', lambda c:
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
    SaveFile(desktop_win))
menu_10.add_separator()
menu_10.add_command(label=lang[11], command=lambda:
    sair(desktop_win))


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
menu_11.add_command(label=lang[29], command=surprise_egg)

menu_1.add_command(label=lang[12], command=SetWinSize)


menu_7.add_command(label=lang[20], command=lambda:
                        fontEdit(1))
menu_7.add_command(label=lang[21], command=lambda:
                        fontEdit(2))


menu_8.add_command(label=lang[22], command=new_window)
menu_8.add_command(label=lang[23], command=clockPlugin)
menu_8.add_separator()
menu_8.add_command(label=lang[10], command=lambda:
    WipeFile(desktop_win))
menu_8.add_separator()


menu_13.add_command(label=plugins.title_1, command=lambda:
    plugins.plugin_1(tk_root=desktop_win, tk_text=TextWidget))

menu_13.add_command(label=plugins.title_2, command=lambda:
    plugins.plugin_2(tk_root=desktop_win, tk_text=TextWidget))

menu_13.add_command(label=plugins.title_3, command=lambda:
    plugins.plugin_3(tk_root=desktop_win, tk_text=TextWidget))

menu_13.add_command(label=plugins.title_4, command=lambda:
    plugins.plugin_4(tk_root=desktop_win, tk_text=TextWidget))

menu_13.add_command(label=plugins.title_5, command=lambda:
    plugins.plugin_5(tk_root=desktop_win, tk_text=TextWidget))

menu_13.add_command(label=plugins.title_6, command=lambda:
    plugins.plugin_6(tk_root=desktop_win, tk_text=TextWidget))

menu_13.add_command(label=plugins.title_7, command=lambda:
    plugins.plugin_7(tk_root=desktop_win, tk_text=TextWidget))
menu_13.add_separator()

menu_13.add_command(label=lang[129], command=plugin_help)


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

# dropdowns/cascades
menu_bar.add_cascade(label=lang[2],menu=menu_10)
menu_bar.add_cascade(label=lang[3],menu=menu_1)
menu_1.add_cascade(label=lang[13], menu=menu_4)
menu_4.add_cascade(label=lang[15], menu=menu_5)
menu_4.add_cascade(label=lang[19], menu=menu_6)
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