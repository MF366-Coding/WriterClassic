
'''
Writer Classic

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

Small contributions by:
    Norb (norbcodes at GitHub)
    Zeca70 (Zeca70 at GitHub)
'''

# Importing the goodies
import sys
from tkinter import * # Window
from tkinter.ttk import * # Not sure
from tkinter import simpledialog as sdg # Inputs with GUI
import tkinter.filedialog as dlg # File Dialogs were never this easy...
import tkinter.messagebox as mb # Never gonna give you up... (Pop-ups)
import webbrowser # Isn't is obvious...
import datetime # Really, bro?
from tkinter.font import Font # Ouchie mama (font, daaah)
import requests # it's a module
import json # search it up

# Windowing
desktop_win = Tk()

with open('config/startup.txt', 'r', encoding='utf-8') as startupFile:
    startAppData = startupFile.read()
    startApp = startAppData[0:1]
    #print(startApp)

desktop_win.iconbitmap("data/app_icon.ico")

response = requests.get('https://api.github.com/repos/MF366-Coding/WriterClassic/releases/latest')
data = json.loads(response.text)
latest_version = data['tag_name']

# Config files
with open('config/lang.txt', 'r') as configLangFile:
    setLang = configLangFile.read()
    #print(setLang[0:2])
    #thisLang2 = setLang[-12:-10]

with open('data/'+str(setLang[0:2])+'.txt', 'r', encoding='utf-8') as usedLangFile:
    usedLang = usedLangFile.read()
    lang = usedLang.split('\n')
    #print(dd)

with open('data/version.txt', 'r', encoding='utf-8') as versionFile:
    appVersionGet = versionFile.read()
    appV = appVersionGet[0:6]
    #print(appV)

with open('config/menu.txt', 'r', encoding='utf-8') as textColor:
    mBg = textColor.read()

with open('config/mfg.txt', 'r', encoding='utf-8') as menuFg:
    mFg = menuFg.read()

with open('config/menu.txt', 'r', encoding='utf-8') as textColor:
    MenuColor = textColor.read()

with open('config/mfg.txt', 'r', encoding='utf-8') as readColor:
    ForegroundColor = readColor.read()

with open('config/font-type.txt', 'r', encoding='utf-8') as fontFile_1:
    FontFamily = fontFile_1.read()

with open('config/font-size.txt', 'r', encoding='utf-8') as fontFile_2:
    FontSize = fontFile_2.read()

# Windowing... again
desktop_win.title(lang[1])

FontSet = Font(family=FontFamily, size=FontSize)

TextWidget = Text(desktop_win, font=FontSet)

with open('config/colour.txt', 'r') as color_bg:
    colorBgData = color_bg.read()

with open('config/geom.txt', 'r') as geom_bg:
    geomValue = geom_bg.read()

with open('config/fg.txt', 'r') as fgConfig:
    foregorundData = fgConfig.read()

with open('config/ct.txt', 'r') as ctConfig:
    ctData = ctConfig.read()

GeomValues = geomValue.split('x')

desktop_win.geometry(geomValue)

TextWidget.configure(bg=colorBgData, fg=foregorundData, width=GeomValues[0], height=GeomValues[1], insertbackground=ctData)
TextWidget.pack()

# Closing the configs
color_bg.close()
fgConfig.close()
geom_bg.close()
ctConfig.close()
configLangFile.close()

def writeStartup(text):
    with open('config/startup.txt', 'w', encoding='utf-8') as startupWriteFile:
        startupWriteFile.write(text)
        startupWriteFile.close()

# Check for Updates
class UpdateCheck:
    @staticmethod
    def check():
        if appV != latest_version:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                webbrowser.open('https://github.com/MF366-Coding/WriterClassic/releases/latest')

    @staticmethod
    def change():
        global startApp
        if startApp == '1':
            writeStartup('0')
        else:
            writeStartup('1')

if startApp == '1':
    UpdateCheck.check()

# Windowing... one more time...
def SetWinSize():
    widthSet = sdg.askinteger(lang[1], lang[57])
    heightSet = sdg.askinteger(lang[1], lang[58])
    TextWidget.configure(width=widthSet, height=heightSet)
    desktop_win.geometry(str(widthSet)+'x'+str(heightSet))
    with open('config/geom.txt', 'w') as geomdata:
        geomdata.write('')
        geomdata.write(str(widthSet)+'x'+str(heightSet))
    geomdata.close()

# Theme Picker
def mudacor(cor, fgcor, cc, bar, bar_sec):
    with open('config/colour.txt', 'w') as again1:
        again1.write('')
        again1.write(cor)
    with open('config/fg.txt', 'w') as again3:
        again3.write('')
        again3.write(fgcor)
    with open('config/ct.txt', 'w') as again2:
        again2.write('')
        again2.write(cc)
    TextWidget.configure(bg=cor, fg=fgcor, insertbackground=cc)
    TextWidget.pack()
    with open('config/menu.txt', 'w') as again4:
        again4.write('')
        again4.write(bar)
    with open('config/mfg.txt', 'w') as again5:
        again5.write('')
        again5.write(bar_sec)
    again1.close()
    again2.close()
    again3.close()
    again4.close()
    again5.close()
    aguardaResposta = mb.askyesno(parent=desktop_win, title=lang[30], message=lang[31])
    if aguardaResposta:
        desktop_win.destroy()

# ragequit
def quickway():
    desktop_win.destroy()

# Setup (Lang files)
def mudaIdioma(idioma, raiz):
    with open('config/lang.txt', 'w') as deleteThat:
        deleteThat.write('')
        deleteThat.write(idioma)
    kkkkSemRiso = mb.askyesno(parent=raiz, title=lang[30], message=lang[31])
    if kkkkSemRiso:
        raiz.destroy()

# Notepad
def new_window():
    newWindow = Toplevel(desktop_win)

    with open('config/menu.txt', 'r', encoding='utf-8') as textColor:
        mBg = textColor.read()

    with open('config/mfg.txt', 'r', encoding='utf-8') as menuFg:
        mFg = menuFg.read()

    with open('config/menu.txt', 'r', encoding='utf-8') as textColor:
        MenuColor = textColor.read()

    with open('config/mfg.txt', 'r', encoding='utf-8') as readColor:
        ForegroundColor = readColor.read()

    # Windowing... yet once more LMAO...
    newWindow.title(lang[22])

    TextWidget = Text(newWindow)

    with open('config/colour.txt', 'r') as color_bg:
        colorBgData = color_bg.read()

    with open('config/geom.txt', 'r') as geom_bg:
        geomValue = geom_bg.read()

    with open('config/fg.txt', 'r') as fgConfig:
        foregorundData = fgConfig.read()

    with open('config/ct.txt', 'r') as ctConfig:
        ctData = ctConfig.read()

    GeomValues = geomValue.split('x')

    newWindow.geometry(geomValue)

    TextWidget.configure(bg=colorBgData, fg=foregorundData, width=GeomValues[0], height=GeomValues[1], insertbackground=ctData)
    TextWidget.pack()

    # Closing what I no longer need
    color_bg.close()
    fgConfig.close()
    geom_bg.close()
    ctConfig.close()
    configLangFile.close()

    newWindow.mainloop()

# Repo
def repo():
    ourRepo = "https://github.com/MF366-Coding/WriterClassic/"

    webbrowser.open(ourRepo, 2)

# Clock
def relogio():
    relog = Toplevel(desktop_win)
    #Stuff

    #Windowing
    relog.title(lang[23])

    TextWidget = Label(relog)

    TextWidget.configure(text=datetime.datetime.now())
    TextWidget.configure(
        font=(100)
        )

    relog.geometry('275x65')

    TextWidget.pack()
    relog.mainloop()

# Text font
def fontEdit(winType):
    if winType == 1:
        fontSize = sdg.askinteger(lang[59], lang[60], minvalue=1)
        with open('config/font-size.txt', 'w') as fontSizeEdit:
            fontSizeEdit.write(str(fontSize))
            fontSizeEdit.close()
            mb.showinfo(lang[1], lang[63])
    else:
        fontType = sdg.askstring(lang[61], lang[62])
        with open('config/font-type.txt', 'w', encoding='utf-8') as fontTypeEdit:
            fontTypeEdit.write(fontType)
            fontTypeEdit.close()
            mb.showinfo(lang[1], lang[63])

# Open the PACKAGE
def abrir(raiz):
    fich = dlg.askopenfilename(parent=raiz, filetypes=[(lang[32], '*.txt'), (lang[33], '*.cfg'), (lang[33], '*.config'), (lang[34], '*.css'), (lang[35], '*.csv'), (lang[36], '*.html'), (lang[37], '*.inf'), (lang[38], '*.info'), (lang[39], '*.ini'), (lang[40], '*.js'), (lang[41], '*.py*'), (lang[42], '*.log'), (lang[43], '*.xml'), (lang[44], '*.1st'), (lang[45], '*.a'), (lang[46], '*.a8s'), (lang[47], '*.ans'), (lang[48], '*.arena'), (lang[49], '*.as'), (lang[50], '*.asa'), (lang[51], '.asm'), (lang[52], '*.md'), (lang[52], '*.mdown')])
    fich_ent2 = open(fich, 'r')
    resultado = fich_ent2.read()
    if len(resultado) > 1:
        abertura = Toplevel(desktop_win)
        abertura.title(lang[3])
        abertura.geometry('615x500')
        quadrado = Frame(abertura)
        quadrado.pack()
        etiqueta_aberta = Label(quadrado, text=resultado, wrap=600)
        etiqueta_aberta.pack()
        #mb.showinfo(title=lang[3], message=resultado)
        fich_entrada = open(fich,'a')
        fich_ent2.close()
    else:
        mb.showinfo(title=lang[1], message=lang[71])
        fich_entrada = open(fich,'a')
        fich_ent2.close()

# Saving as
def salvar(raiz,TextWidget):
    dados = TextWidget.get('0.0', END)
    ficheiro = dlg.askopenfilename(parent=raiz, filetypes=[(lang[32], '*.txt'), (lang[33], '*.cfg'), (lang[33], '*.config'), (lang[34], '*.css'), (lang[35], '*.csv'), (lang[36], '*.html'), (lang[37], '*.inf'), (lang[38], '*.info'), (lang[39], '*.ini'), (lang[40], '*.js'), (lang[41], '*.py*'), (lang[42], '*.log'), (lang[43], '*.xml'), (lang[44], '*.1st'), (lang[45], '*.a'), (lang[46], '*.a8s'), (lang[47], '*.ans'), (lang[48], '*.arena'), (lang[49], '*.as'), (lang[50], '*.asa'), (lang[51], '.asm'), (lang[52], '*.md'), (lang[52], '*.mdown')])
    fich_saida = open(ficheiro, 'w')
    fich_saida.write(dados)
    fich_saida.close()

# Saving
def salvarA(raiz, TextWidget):
    dados = TextWidget.get('0.0', END)
    ficheiro = dlg.askopenfilename(parent=raiz, filetypes=[(lang[32], '*.txt'), (lang[33], '*.cfg'), (lang[33], '*.config'), (lang[34], '*.css'), (lang[35], '*.csv'), (lang[36], '*.html'), (lang[37], '*.inf'), (lang[38], '*.info'), (lang[39], '*.ini'), (lang[40], '*.js'), (lang[41], '*.py*'), (lang[42], '*.log'), (lang[43], '*.xml'), (lang[44], '*.1st'), (lang[45], '*.a'), (lang[46], '*.a8s'), (lang[47], '*.ans'), (lang[48], '*.arena'), (lang[49], '*.as'), (lang[50], '*.asa'), (lang[51], '.asm'), (lang[52], '*.md'), (lang[52], '*.mdown')])
    fich_saida = open(ficheiro, 'a')
    fich_saida.write(dados)
    fich_saida.close()

# Whatever... (File Eraser)
def formatar(raiz):
    pois = mb.askyesno(title=lang[55], message=lang[56])
    if pois:
        ficheiro = dlg.askopenfilename(parent=raiz, filetypes=[(lang[32], '*.txt'), (lang[33], '*.cfg'), (lang[33], '*.config'), (lang[34], '*.css'), (lang[35], '*.csv'), (lang[36], '*.html'), (lang[37], '*.inf'), (lang[38], '*.info'), (lang[39], '*.ini'), (lang[40], '*.js'), (lang[41], '*.py*'), (lang[42], '*.log'), (lang[43], '*.xml'), (lang[44], '*.1st'), (lang[45], '*.a'), (lang[46], '*.a8s'), (lang[47], '*.ans'), (lang[48], '*.arena'), (lang[49], '*.as'), (lang[50], '*.asa'), (lang[51], '.asm'), (lang[52], '*.md'), (lang[52], '*.mdown')])
        fich_teste = open(ficheiro, 'r')
        fich_test = fich_teste.read()
        if len(fich_test) != 0:
            fich_saida = open(ficheiro, 'w')
            fich_saida.write('')
            fich_saida.close()
        else:
            mb.showinfo(title=lang[1], message=lang[71])
            fich_teste.close()

# Non-raged quit
def sair(raiz):
    confirm = mb.askyesno(title=lang[53], message=lang[54])
    if confirm:
        raiz.destroy()

#Abrir os Créditos
def creditos_abertos():
    mb.showinfo(title=lang[28], message=lang[65])

#Abrir o Easter Egg
def surprise_egg():
    askNow = sdg.askstring(lang[29], lang[66])

    if askNow == 'Nice stuff!!':
        webbrowser.open('https://www.youtube.com/watch?v=W6FG7yVUaKQ')

    elif askNow == 'Scan':
        mb.showerror("Your PC has virus!", "Press Alt+F4 to remove all viruses!!!\nDo it!!!")

    else:
        mb.showerror(lang[29], lang[67])

#Abrir a Ajuda
def ajuda():
    ourWebsite = "https://github.com/MF366-Coding/WriterClassic#help"

    webbrowser.open(ourWebsite, 2)

#Abrir as informações
def sobre(thing2, thing3):
    with open(thing2, thing3, encoding='utf-8') as about_d:
        about_data = about_d.read()
    mb.showinfo(title=lang[64], message=about_data)
    about_d.close()

def resetWriter(rootWin):
    askSOS = mb.askyesno(lang[77], lang[78])
    if askSOS:
        with open('config/font-size.txt', 'w') as fontSizeEdit:
            fontSizeEdit.write('12')
            fontSizeEdit.close()

        with open('config/font-type.txt', 'w', encoding='utf-8') as fontTypeEdit:
            fontTypeEdit.write('Ubuntu Mono')
            fontTypeEdit.close()

        mudaIdioma('en', rootWin)

        mudacor('black', 'white', 'white', 'black', 'white')

        desktop_win.geometry('600x400')
        with open('config/geom.txt', 'w') as geomdata:
            geomdata.write('')
            geomdata.write('600x400')
            geomdata.close()

class InternetOnWriter:
    @staticmethod
    def Website():
        askForLink = sdg.askstring(lang[80], lang[91])
        if askForLink != ' ' or askForLink != '':
            if sys.platform == "win32":
                webbrowser.open(askForLink)
                # for some reason this opens IExplorer in Windows 10?!
                # which will send you to Edge?!
                # ill try to fix this in the future
            elif sys.platform == "linux" or "darwin":
                webbrowser.open(askForLink)

    @staticmethod
    def Search(engine):
        if engine == 'google':
            askForTyping = sdg.askstring(lang[83], lang[90])
            if askForTyping != '':
                for i in askForTyping:
                    typed = askForTyping.replace(' ', '+')
                webbrowser.open('https://www.google.com/search?q='+typed)
        elif engine == 'bing':
            askForTyping = sdg.askstring(lang[82], lang[90])
            if askForTyping != '':
                for i in askForTyping:
                    typed = askForTyping.replace(' ', '+')
                webbrowser.open('https://www.bing.com/search?q='+typed)

InternetOnWriter

def commandPrompt():
    askNow = sdg.askstring(lang[68], lang[69])

    if askNow == 'open' or askNow == 'openfile':
        abrir(desktop_win)

    elif askNow == 'about':
        sobre('data/about.txt', 'r')

    elif askNow == 'help':
        ajuda()

    elif askNow == 'fun' or askNow == 'egg':
        surprise_egg()

    elif askNow == 'data':
        creditos_abertos()

    elif askNow == 'exit' or askNow == 'quit':
        sair(desktop_win)

    elif askNow == 'clear':
        formatar(desktop_win)

    elif askNow == 'savefile':
        salvarA(desktop_win, TextWidget)

    elif askNow == 'save':
        salvar(desktop_win, TextWidget)

    elif askNow == 'WriterClassic.Plugin.clock.RUN()':
        relogio()

    elif askNow == 'FontEdit.family()':
        fontEdit(2)

    elif askNow == 'FontEdit.size()':
        fontEdit(1)

    elif askNow == 'ragequit':
        quickway()

    elif askNow == 'repo':
        repo()

    elif askNow == 'notes':
        new_window()

    elif askNow == 'WINDOW.geometry()':
        SetWinSize()

    else:
        mb.showerror(lang[68], lang[70])

# Key bindings

desktop_win.bind('<Control-o>', lambda b:
    abrir(desktop_win))

desktop_win.bind('<Control-s>', lambda c:
    salvar(desktop_win, TextWidget))

desktop_win.bind('<Control-a>', lambda e:
    sobre('data/about.txt', 'r'))

desktop_win.bind('<Control-h>', lambda f:
    ajuda())

desktop_win.bind('<Control-d>', lambda g:
    mudacor('black', 'white', 'white', 'dark grey', 'black'))

desktop_win.bind('<Control-l>', lambda h:
    mudacor('white', 'black', 'black', 'black', 'white'))

desktop_win.bind('<Control-g>', lambda j:
    SetWinSize())

desktop_win.bind('<Control-r>', lambda l:
    relogio())

desktop_win.bind('<Control-w>', lambda m:
    commandPrompt())


#Ao abrir o Writer, isto acontecerá...
if __name__ == '__main__':

    #Configurar a barra de menu
    barra_menu = Menu(desktop_win)
    barra_menu.configure(background=mBg, foreground=mFg)

    #Adicionar o Menu Ficheiro
    ficheiro_menu = Menu(barra_menu)
    ficheiro_menu.add_command(label=lang[7], command=lambda:
        abrir(desktop_win))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=lang[8], command=lambda:
        salvarA(desktop_win, TextWidget))
    ficheiro_menu.add_command(label = lang[9], command=lambda:
        salvar(desktop_win,TextWidget))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=lang[10], command=lambda:
        formatar(desktop_win))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=lang[11], command=lambda:
        sair(desktop_win))

    #Adicionar o Menu Informações
    editar_menu = Menu(barra_menu)
    editar_menu.add_command(label=lang[75], command=lambda:
        UpdateCheck.check())
    editar_menu.add_separator()
    editar_menu.add_command(label=lang[25], command=lambda:
        sobre('data/about.txt', 'r'))
    editar_menu.add_command(label=lang[26], command=lambda:
        ajuda())
    editar_menu.add_command(label=lang[27], command=repo)
    editar_menu.add_separator()
    editar_menu.add_command(label=lang[28], command=creditos_abertos)
    editar_menu.add_separator()
    editar_menu.add_command(label=lang[29], command=surprise_egg)


    #Adicionar as configurações necessárias para os outros menus
    ver_menu = Menu(barra_menu)
    ver_1_m = Menu(ver_menu)
    ver_3_m = Menu(ver_1_m)
    ver_5_m = Menu(ver_menu)
    ver_4_m = Menu(ver_5_m)
    ver_7_m = Menu(ver_5_m)
    newMenuEdit = Menu(ver_menu)
    b_m = Menu(barra_menu)
    c_m = Menu(b_m)
    z_m = Menu(b_m)

    ver_menu.add_command(label=lang[12], command=SetWinSize)

    # menu fonts
    newMenuEdit.add_command(label=lang[20], command=lambda:
                            fontEdit(1))
    newMenuEdit.add_command(label=lang[21], command=lambda:
                            fontEdit(2))

    #Adicionar o Menu Plugins
    b_m.add_command(label=lang[22], command=new_window)
    b_m.add_command(label=lang[23], command=relogio)

    c_m.add_command(label=lang[81], command=lambda:
                    InternetOnWriter.Website())
    c_m.add_separator()
    c_m.add_command(label=lang[87], command=lambda:
                    InternetOnWriter.Search('google'))
    c_m.add_command(label=lang[86], command=lambda:
                    InternetOnWriter.Search('bing'))

    #Adicionar temas da comunidade
    z_m.add_command(label='Black Hole', command=lambda:
        mudacor('black', 'white', 'white', 'black', 'white'))
    z_m.add_command(label='Blue Bubble', command=lambda:
        mudacor('white', 'blue', 'blue', 'white', 'dark blue'))
    z_m.add_command(label='Green Bubble', command=lambda:
        mudacor('white', 'green', 'green', 'white', 'dark green'))
    z_m.add_command(label='Red Bubble', command=lambda:
        mudacor('white', 'red', 'red', 'white', 'brown'))
    z_m.add_command(label='Diving and Arriving', command=lambda:
        mudacor('#1697a1', '#05011f', '#05011f', '#075d63', 'black'))
    z_m.add_command(label='TOP SECRET!', command=lambda:
        mudacor('black', '#ff2626', '#ff2626', 'black', '#fa7d7d'))
    z_m.add_command(label='Forgotten', command=lambda:
        mudacor('#470404', 'white', 'white', '#260202', '#e09d9d'))

    #Adicionar o Menu Definições
    a_m = Menu(barra_menu)
    a_m.add_command(label='English', command=lambda:
        mudaIdioma('en', desktop_win))
    a_m.add_command(label='Español (España)', command=lambda:
        mudaIdioma('es', desktop_win))
    a_m.add_command(label='Français (France)', command=lambda:
        mudaIdioma('fr', desktop_win))
    a_m.add_command(label='Italiano (Italia)', command=lambda:
        mudaIdioma('it', desktop_win))
    a_m.add_command(label='Português (Brasil)', command=lambda:
        mudaIdioma('br', desktop_win))
    a_m.add_command(label='Português (Portugal)', command=lambda:
        mudaIdioma('pt', desktop_win))
    a_m.add_command(label='Slovenčina (Slovensko)', command=lambda:
        mudaIdioma('sk', desktop_win))
    a_m.add_separator()
    a_m.add_command(label=lang[74], command=lambda:
        UpdateCheck.change())
    a_m.add_separator()
    a_m.add_command(label=lang[76], command=lambda:
        resetWriter(desktop_win))

    #Adicionar os Temas (Temas Regulares)
    ver_4_m.add_command(label=lang[16], command=lambda:
        mudacor('white', 'black', 'black', 'black', 'white'))
    ver_4_m.add_command(label=lang[17], command=lambda:
        mudacor('black', 'white', 'white', 'dark grey', 'black'))
    ver_4_m.add_separator()
    ver_4_m.add_command(label=lang[18], command=lambda:
        mudacor('grey', 'black', 'black', 'black', 'white'))

    #Adicionar os Temas (Temas Modernos)
    ver_7_m.add_command(label='Light Yellow', command=lambda:
        mudacor('light yellow', 'black', 'black', '#f5b949', 'black'))
    ver_7_m.add_command(label='Magic', command=lambda:
        mudacor('purple', 'white', 'white', '#290340', 'white'))
    ver_7_m.add_command(label='Through the Sky', command=lambda:
        mudacor('light blue', 'black', 'black', '#031882', 'white'))
    ver_7_m.add_command(label='Light Green', command=lambda:
        mudacor('light green', 'black', 'black', '#0e2414', 'white'))
    ver_7_m.add_command(label='Codetime', command=lambda:
        mudacor('black', 'green', 'green', 'black', 'light green'))
    ver_7_m.add_command(label='Darkest Night Ever', command=lambda:
        mudacor('#040114', '#e8a78e', '#e8a78e', 'black', '#e8a78e'))
    ver_7_m.add_command(label='Dark Forest', command=lambda:
        mudacor('#0e2414', '#c0db7b', '#c0db7b', '#040d07', '#ccf0c5'))
    ver_7_m.add_command(label='Christmas Night', command=lambda:
       mudacor('#020421', '#a5a9e8', '#a5a9e8', '#020312', '#cbcef2'))
    ver_7_m.add_command(label='Silent Night', command=lambda:
        mudacor('#020421','pink', 'pink', '#020312', '#ebd1ed'))

    #Configurar cores do Menu
    ficheiro_menu.configure(background=MenuColor, foreground=ForegroundColor)
    editar_menu.configure(background=MenuColor, foreground=ForegroundColor)
    ver_menu.configure(background=MenuColor, foreground=ForegroundColor)
    ver_1_m.configure(background=MenuColor, foreground=ForegroundColor)
    ver_3_m.configure(background=MenuColor, foreground=ForegroundColor)
    ver_4_m.configure(background=MenuColor, foreground=ForegroundColor)
    ver_5_m.configure(background=MenuColor, foreground=ForegroundColor)
    ver_7_m.configure(background=MenuColor, foreground=ForegroundColor)
    newMenuEdit.configure(background=MenuColor, foreground=ForegroundColor)
    a_m.configure(background=MenuColor, foreground=ForegroundColor)
    b_m.configure(background=MenuColor, foreground=ForegroundColor)
    c_m.configure(background=MenuColor, foreground=ForegroundColor)
    z_m.configure(background=MenuColor, foreground=ForegroundColor)

#Adicionar menus "cascade"
barra_menu.add_cascade(label=lang[2],menu=ficheiro_menu)
barra_menu.add_cascade(label=lang[3],menu=ver_menu)
ver_menu.add_cascade(label=lang[13], menu=ver_5_m)
ver_5_m.add_cascade(label=lang[15], menu=ver_4_m)
ver_5_m.add_cascade(label=lang[19], menu=ver_7_m)
ver_menu.add_cascade(label=lang[14], menu=newMenuEdit)
barra_menu.add_cascade(label=lang[4], menu=b_m)
b_m.add_cascade(label=lang[24], menu=z_m)
b_m.add_cascade(label=lang[79], menu=c_m)
barra_menu.add_cascade(label=lang[5], menu=a_m)
barra_menu.add_cascade(label=lang[6], menu=editar_menu)

#Configurar o menu da desktop_win
desktop_win.configure(menu=barra_menu)

#Efetuar o mainloop da desktop_win
desktop_win.mainloop()
