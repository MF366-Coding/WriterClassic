
'''

Writer Classic

Powered by: in Python 3.10.8

Official Repo:
    https://github.com/MF366-Coding/WriterClassic

Find me in this spots:
    https://github.com/MF366-Coding
    Discord: MF366#8679
    https://www.youtube.com/channel/UC-eyGQUY7mICmAuLSI2ZO5A/

Original idea by: MF366
Developed by: MF366

'''

# Improting the goodies
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
janela = Tk()

with open('config/startup.txt', 'r', encoding='utf-8') as startupFile:
    startAppData = startupFile.read()
    startApp = startAppData[0:1]
    #print(startApp)

response = requests.get('https://api.github.com/repos/MF366-Coding/WriterClassic/releases/latest')
data = json.loads(response.text)
latest_version = data['tag_name']

# Config files
with open('config/lang.txt', 'r') as langset:
    thisLang = langset.read()
    #print(thisLang[0:2])
    #thisLang2 = thisLang[-12:-10]
    
with open('data/'+str(thisLang[0:2])+'.txt', 'r', encoding='utf-8') as myLang2:
    myLang = myLang2.read()
    dd = myLang.split('\n')
    #print(dd)
    
with open('data/version.txt', 'r', encoding='utf-8') as versionFile:
    appVersionGet = versionFile.read()
    appV = appVersionGet[0:6]
    #print(appV)

with open('config/menu.txt', 'r', encoding='utf-8') as menuColor:
    mBg = menuColor.read()

with open('config/mfg.txt', 'r', encoding='utf-8') as menuFg:
    mFg = menuFg.read()

with open('config/menu.txt', 'r', encoding='utf-8') as corLeitura:
    corMenu = corLeitura.read()

with open('config/mfg.txt', 'r', encoding='utf-8') as corFgLer:
    colorFg = corFgLer.read()

with open('config/font-type.txt', 'r', encoding='utf-8') as fonteee:
    fontee = fonteee.read()
    
with open('config/font-size.txt', 'r', encoding='utf-8') as fonteeee:
    Fontee = fonteeee.read()
    
# Windowing... again
janela.title(dd[1])

fonte = Font(family=fontee, size=Fontee)

texto = Text(janela, font=fonte)

with open('config/colour.txt', 'r') as cbg:
    cbg2 = cbg.read()

with open('config/geom.txt', 'r') as gbg:
    geom2 = gbg.read()

with open('config/fg.txt', 'r') as fgcnf:
    fogr = fgcnf.read()

with open('config/ct.txt', 'r') as ccc:
    oc = ccc.read()

ff = geom2.split('x')

janela.geometry(geom2)

texto.configure(bg=cbg2, fg=fogr, width=ff[0], height=ff[1], insertbackground=oc)
texto.pack()

# Closing the configs
cbg.close()
fgcnf.close()
gbg.close()
ccc.close()
langset.close()

def writeStartup(text):
    with open('config/startup.txt', 'w', encoding='utf-8') as startupWriteFile:
        startupWriteFile.write(text)
        startupWriteFile.close()

# Check for Updates
class UpdateCheck:
    def check():
        if appV != latest_version:
            askForUpdate = mb.askyesno(dd[72], dd[73])
            if askForUpdate:
                webbrowser.open('https://github.com/MF366-Coding/WriterClassic/releases/latest')

    def change():
        global startApp
        if startApp == '1':
            writeStartup('0')
        else:
            writeStartup('1')

if startApp == '1':
    UpdateCheck.check()
    
# Windowing... one more time...
def janelageometrica1():
    widthSet = sdg.askinteger(dd[1], dd[57])
    heightSet = sdg.askinteger(dd[1], dd[58])
    texto.configure(width=widthSet, height=heightSet)
    janela.geometry(str(widthSet)+'x'+str(heightSet))
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
    texto.configure(bg=cor, fg=fgcor, insertbackground=cc)
    texto.pack()
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
    aguardaResposta = mb.askyesno(parent=janela, title=dd[30], message=dd[31])
    if aguardaResposta:
        janela.destroy()

# ragequit
def quickway():
    janela.destroy()

# Setup (Lang files)
def mudaIdioma(idioma, raiz):
    with open('config/lang.txt', 'w') as deleteThat:
        deleteThat.write('')
        deleteThat.write(idioma)
    kkkkSemRiso = mb.askyesno(parent=raiz, title=dd[30], message=dd[31])
    if kkkkSemRiso:
        raiz.destroy()

# Notepad
def new_window():
    newWindow = Toplevel(janela)

    with open('config/menu.txt', 'r', encoding='utf-8') as menuColor:
        mBg = menuColor.read()

    with open('config/mfg.txt', 'r', encoding='utf-8') as menuFg:
        mFg = menuFg.read()

    with open('config/menu.txt', 'r', encoding='utf-8') as corLeitura:
        corMenu = corLeitura.read()

    with open('config/mfg.txt', 'r', encoding='utf-8') as corFgLer:
        colorFg = corFgLer.read()

    # Windowing... yet once more LMAO...
    newWindow.title(dd[22])

    texto = Text(newWindow)

    with open('config/colour.txt', 'r') as cbg:
        cbg2 = cbg.read()

    with open('config/geom.txt', 'r') as gbg:
        geom2 = gbg.read()

    with open('config/fg.txt', 'r') as fgcnf:
        fogr = fgcnf.read()

    with open('config/ct.txt', 'r') as ccc:
        oc = ccc.read()

    ff = geom2.split('x')

    newWindow.geometry(geom2)

    texto.configure(bg=cbg2, fg=fogr, width=ff[0], height=ff[1], insertbackground=oc)
    texto.pack()

    # Closing what I no longer need
    cbg.close()
    fgcnf.close()
    gbg.close()
    ccc.close()
    langset.close()

    newWindow.mainloop()

# Repo
def repo():
    ourRepo = "https://github.com/MF366-Coding/WriterClassic/"

    webbrowser.open(ourRepo, 2)

# Clock
def relogio():
    relog = Toplevel(janela)
    #Stuff

    #Windowing
    relog.title(dd[23])

    texto = Label(relog)

    texto.configure(text=datetime.datetime.now())
    texto.configure(
        font=(100)
        )

    relog.geometry('275x65')

    texto.pack()
    relog.mainloop()

# Text font
def fontEdit(winType):
    if winType == 1:
        fontSize = sdg.askinteger(dd[59], dd[60], minvalue=1)
        with open('config/font-size.txt', 'w') as fontSizeEdit:
            fontSizeEdit.write(str(fontSize))
            fontSizeEdit.close()
            mb.showinfo(dd[1], dd[63])
    else:
        fontType = sdg.askstring(dd[61], dd[62])
        with open('config/font-type.txt', 'w', encoding='utf-8') as fontTypeEdit:
            fontTypeEdit.write(fontType)
            fontTypeEdit.close()
            mb.showinfo(dd[1], dd[63])

# Open the PACKAGE
def abrir(raiz):
    fich = dlg.askopenfilename(parent=raiz, filetypes=[(dd[32], '*.txt'), (dd[33], '*.cfg'), (dd[33], '*.config'), (dd[34], '*.css'), (dd[35], '*.csv'), (dd[36], '*.html'), (dd[37], '*.inf'), (dd[38], '*.info'), (dd[39], '*.ini'), (dd[40], '*.js'), (dd[41], '*.py*'), (dd[42], '*.log'), (dd[43], '*.xml'), (dd[44], '*.1st'), (dd[45], '*.a'), (dd[46], '*.a8s'), (dd[47], '*.ans'), (dd[48], '*.arena'), (dd[49], '*.as'), (dd[50], '*.asa'), (dd[51], '.asm'), (dd[52], '*.md'), (dd[52], '*.mdown')])
    fich_ent2 = open(fich, 'r')
    resultado = fich_ent2.read()
    if len(resultado) > 1:
        abertura = Toplevel(janela)
        abertura.title(dd[3])
        abertura.geometry('615x500')
        quadrado = Frame(abertura)
        quadrado.pack()
        etiqueta_aberta = Label(quadrado, text=resultado, wrap=600)
        etiqueta_aberta.pack()
        #mb.showinfo(title=dd[3], message=resultado)
        fich_entrada = open(fich,'a')
        fich_ent2.close()
    else:
        mb.showinfo(title=dd[1], message=dd[71])
        fich_entrada = open(fich,'a')
        fich_ent2.close()

# Saving as
def salvar(raiz,texto):
    dados = texto.get('0.0', END)
    ficheiro = dlg.askopenfilename(parent=raiz, filetypes=[(dd[32], '*.txt'), (dd[33], '*.cfg'), (dd[33], '*.config'), (dd[34], '*.css'), (dd[35], '*.csv'), (dd[36], '*.html'), (dd[37], '*.inf'), (dd[38], '*.info'), (dd[39], '*.ini'), (dd[40], '*.js'), (dd[41], '*.py*'), (dd[42], '*.log'), (dd[43], '*.xml'), (dd[44], '*.1st'), (dd[45], '*.a'), (dd[46], '*.a8s'), (dd[47], '*.ans'), (dd[48], '*.arena'), (dd[49], '*.as'), (dd[50], '*.asa'), (dd[51], '.asm'), (dd[52], '*.md'), (dd[52], '*.mdown')])
    fich_saida = open(ficheiro, 'w')
    fich_saida.write(dados)
    fich_saida.close()

# Saving
def salvarA(raiz, texto):
    dados = texto.get('0.0', END)
    ficheiro = dlg.askopenfilename(parent=raiz, filetypes=[(dd[32], '*.txt'), (dd[33], '*.cfg'), (dd[33], '*.config'), (dd[34], '*.css'), (dd[35], '*.csv'), (dd[36], '*.html'), (dd[37], '*.inf'), (dd[38], '*.info'), (dd[39], '*.ini'), (dd[40], '*.js'), (dd[41], '*.py*'), (dd[42], '*.log'), (dd[43], '*.xml'), (dd[44], '*.1st'), (dd[45], '*.a'), (dd[46], '*.a8s'), (dd[47], '*.ans'), (dd[48], '*.arena'), (dd[49], '*.as'), (dd[50], '*.asa'), (dd[51], '.asm'), (dd[52], '*.md'), (dd[52], '*.mdown')])
    fich_saida = open(ficheiro, 'a')
    fich_saida.write(dados)
    fich_saida.close()

# Whatever... (File Eraser)
def formatar(raiz):
    pois = mb.askyesno(title=dd[55], message=dd[56])
    if pois:
        ficheiro = dlg.askopenfilename(parent=raiz, filetypes=[(dd[32], '*.txt'), (dd[33], '*.cfg'), (dd[33], '*.config'), (dd[34], '*.css'), (dd[35], '*.csv'), (dd[36], '*.html'), (dd[37], '*.inf'), (dd[38], '*.info'), (dd[39], '*.ini'), (dd[40], '*.js'), (dd[41], '*.py*'), (dd[42], '*.log'), (dd[43], '*.xml'), (dd[44], '*.1st'), (dd[45], '*.a'), (dd[46], '*.a8s'), (dd[47], '*.ans'), (dd[48], '*.arena'), (dd[49], '*.as'), (dd[50], '*.asa'), (dd[51], '.asm'), (dd[52], '*.md'), (dd[52], '*.mdown')])
        fich_teste = open(ficheiro, 'r')
        fich_test = fich_teste.read()
        if len(fich_test) != 0:
            fich_saida = open(ficheiro, 'w')
            fich_saida.write('')
            fich_saida.close()
        else:
            mb.showinfo(title=dd[1], message=dd[71])
            fich_teste.close()

# Non-raged quit
def sair(raiz):
    confirm = mb.askyesno(title=dd[53], message=dd[54])
    if confirm:
        raiz.destroy()

#Abrir os Créditos
def creditos_abertos():
    mb.showinfo(title=dd[28], message=dd[65])

#Abrir o Easter Egg
def surprise_egg():
    askNow = sdg.askstring(dd[29], dd[66])
    
    if askNow == 'Nice stuff!!':
        webbrowser.open('https://www.youtube.com/watch?v=W6FG7yVUaKQ')
    
    elif askNow == 'Scan':
        mb.showerror("Your PC has virus!", "Press Alt+F4 to remove all viruses!!!\nDo it!!!")
    
    else:
        mb.showerror(dd[29], dd[67])
    
#Abrir a Ajuda
def ajuda():
    ourWebsite = "https://github.com/MF366-Coding/WriterClassic#help"

    webbrowser.open(ourWebsite, 2)

#Abrir as informações
def sobre(thing2, thing3):
    with open(thing2, thing3, encoding='utf-8') as about_d:
        about_data = about_d.read()
    mb.showinfo(title=dd[64], message=about_data)
    about_d.close()

def resetWriter(rootWin):
    askSOS = mb.askyesno(dd[77], dd[78])
    if askSOS:
        with open('config/font-size.txt', 'w') as fontSizeEdit:
            fontSizeEdit.write('12')
            fontSizeEdit.close()
                    
        with open('config/font-type.txt', 'w', encoding='utf-8') as fontTypeEdit:
            fontTypeEdit.write('Ubuntu Mono')
            fontTypeEdit.close()
        
        mudaIdioma('en', rootWin)
        
        mudacor('black', 'white', 'white', 'black', 'white')
        
        janela.geometry('600x400')
        with open('config/geom.txt', 'w') as geomdata:
            geomdata.write('')
            geomdata.write('600x400')
            geomdata.close()

def commandPrompt():
    askNow = sdg.askstring(dd[68], dd[69])
    
    if askNow == 'open' or askNow == 'openfile':
        abrir(janela)
        
    elif askNow == 'about':
        sobre('data/about.txt', 'r')
        
    elif askNow == 'help':
        ajuda()
        
    elif askNow == 'fun' or askNow == 'egg':
        surprise_egg()
        
    elif askNow == 'data':
        creditos_abertos()
        
    elif askNow == 'exit' or askNow == 'quit':
        sair(janela)
        
    elif askNow == 'clear':
        formatar(janela)

    elif askNow == 'savefile':
        salvarA(janela, texto)

    elif askNow == 'save':
        salvar(janela, texto)
        
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
        janelageometrica1()
        
    else:
        mb.showerror(dd[68], dd[70])

# Key bindings

janela.bind('<Control-o>', lambda b:
    abrir(janela))

janela.bind('<Control-s>', lambda c:
    salvar(janela, texto))

janela.bind('<Control-a>', lambda e:
    sobre('data/about.txt', 'r'))

janela.bind('<Control-h>', lambda f:
    ajuda())

janela.bind('<Control-d>', lambda g:
    mudacor('black', 'white', 'white', 'dark grey', 'black'))

janela.bind('<Control-l>', lambda h:
    mudacor('white', 'black', 'black', 'black', 'white'))

janela.bind('<Control-g>', lambda j:
    janelageometrica1(janela,600,400))

janela.bind('<Control-r>', lambda l:
    relogio())
    
janela.bind('<Control-w>', lambda m:
    commandPrompt())


#Ao abrir o Writer, isto acontecerá...
if __name__ == '__main__':

    #Configurar a barra de menu
    barra_menu = Menu(janela)
    barra_menu.configure(background=mBg, foreground=mFg)

    #Adicionar o Menu Ficheiro
    ficheiro_menu = Menu(barra_menu)
    ficheiro_menu.add_command(label=dd[7], command=lambda:
        abrir(janela))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=dd[8], command=lambda:
        salvarA(janela, texto))
    ficheiro_menu.add_command(label = dd[9], command=lambda:
        salvar(janela,texto))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=dd[10], command=lambda:
        formatar(janela))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=dd[11], command=lambda:
        sair(janela))

    #Adicionar o Menu Informações
    editar_menu = Menu(barra_menu)
    editar_menu.add_command(label=dd[75], command=lambda:
        UpdateCheck.check())
    editar_menu.add_separator()
    editar_menu.add_command(label=dd[25], command=lambda:
        sobre('data/about.txt', 'r'))
    editar_menu.add_command(label=dd[26], command=lambda:
        ajuda())
    editar_menu.add_command(label=dd[27], command=repo)
    editar_menu.add_separator()
    editar_menu.add_command(label=dd[28], command=creditos_abertos)
    editar_menu.add_separator()
    editar_menu.add_command(label=dd[29], command=surprise_egg)


    #Adicionar as configurações necessárias para os outros menus
    ver_menu = Menu(barra_menu)
    ver_1_m = Menu(ver_menu)
    ver_3_m = Menu(ver_1_m)
    ver_5_m = Menu(ver_menu)
    ver_4_m = Menu(ver_5_m)
    ver_7_m = Menu(ver_5_m)
    newMenuEdit = Menu(ver_menu)
    b_m = Menu(barra_menu)
    z_m = Menu(b_m)

    ver_menu.add_command(label=dd[12], command=janelageometrica1)

    # menu fonts
    newMenuEdit.add_command(label=dd[20], command=lambda:
                            fontEdit(1))
    newMenuEdit.add_command(label=dd[21], command=lambda:
                            fontEdit(2))

    #Adicionar o Menu Plugins
    b_m.add_command(label=dd[22], command=new_window)
    b_m.add_command(label=dd[23], command=relogio)
    
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
        mudaIdioma('en', janela))
    a_m.add_command(label='Español (España)', command=lambda:
        mudaIdioma('es', janela))
    a_m.add_command(label='Français (France)', command=lambda:
        mudaIdioma('fr', janela))
    a_m.add_command(label='Italiano (Italia)', command=lambda:
        mudaIdioma('it', janela))
    a_m.add_command(label='Português (Brasil)', command=lambda:
        mudaIdioma('br', janela))
    a_m.add_command(label='Português (Portugal)', command=lambda:
        mudaIdioma('pt', janela))
    a_m.add_command(label='Slovenčina (Slovensko)', command=lambda:
        mudaIdioma('sk', janela))
    a_m.add_separator()
    a_m.add_command(label=dd[74], command=lambda:
        UpdateCheck.change())
    a_m.add_separator()
    a_m.add_command(label=dd[76], command=lambda:
        resetWriter(janela))

    #Adicionar os Temas (Temas Regulares)
    ver_4_m.add_command(label=dd[16], command=lambda:
        mudacor('white', 'black', 'black', 'black', 'white'))
    ver_4_m.add_command(label=dd[17], command=lambda:
        mudacor('black', 'white', 'white', 'dark grey', 'black'))
    ver_4_m.add_separator()
    ver_4_m.add_command(label=dd[18], command=lambda:
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
    ficheiro_menu.configure(background=corMenu, foreground=colorFg)
    editar_menu.configure(background=corMenu, foreground=colorFg)
    ver_menu.configure(background=corMenu, foreground=colorFg)
    ver_1_m.configure(background=corMenu, foreground=colorFg)
    ver_3_m.configure(background=corMenu, foreground=colorFg)
    ver_4_m.configure(background=corMenu, foreground=colorFg)
    ver_5_m.configure(background=corMenu, foreground=colorFg)
    ver_7_m.configure(background=corMenu, foreground=colorFg)
    newMenuEdit.configure(background=corMenu, foreground=colorFg)
    a_m.configure(background=corMenu, foreground=colorFg)
    b_m.configure(background=corMenu, foreground=colorFg)
    z_m.configure(background=corMenu, foreground=colorFg)

#Adicionar menus "cascade"
barra_menu.add_cascade(label=dd[2],menu=ficheiro_menu)
barra_menu.add_cascade(label=dd[3],menu=ver_menu)
ver_menu.add_cascade(label=dd[13], menu=ver_5_m)
ver_5_m.add_cascade(label=dd[15], menu=ver_4_m)
ver_5_m.add_cascade(label=dd[19], menu=ver_7_m)
ver_menu.add_cascade(label=dd[14], menu=newMenuEdit)
barra_menu.add_cascade(label=dd[4], menu=b_m)
b_m.add_cascade(label=dd[24], menu=z_m)
barra_menu.add_cascade(label=dd[5], menu=a_m)
barra_menu.add_cascade(label=dd[6], menu=editar_menu)

#Configurar o menu da janela
janela.configure(menu=barra_menu)

#Efetuar o mainloop da janela
janela.mainloop()
