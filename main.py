'''

Writer Classic

Made in Python 3

Original idea by: Mega Informática
Developed by: Mega Informática

'''

#Importar os módulos necessários
from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog as dlg
import tkinter.messagebox as mb
import webbrowser
import datetime

#Criar a janela
janela = Tk()

#Abrir os ficheiros de configuração
with open('config/lang.txt', 'r') as langset:
    thisLang = langset.read()

with open('data/'+str(thisLang)+'.txt', 'r', encoding='utf-8') as myLang2:
    myLang = myLang2.read()
    dd = myLang.split('//')

with open('config/menu.txt', 'r', encoding='utf-8') as menuColor:
    mBg = menuColor.read()

with open('config/mfg.txt', 'r', encoding='utf-8') as menuFg:
    mFg = menuFg.read()

with open('config/menu.txt', 'r', encoding='utf-8') as corLeitura:
    corMenu = corLeitura.read()

with open('config/mfg.txt', 'r', encoding='utf-8') as corFgLer:
    colorFg = corFgLer.read()

#Configurar o texto e a janela
janela.title(dd[0])



texto = Text(janela)

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

#Fechar os ficheiros
cbg.close()
fgcnf.close()
gbg.close()
ccc.close()
langset.close()


def janelageometrica1(indicar,usar,nao):
    indicar.geometry(str(usar)+'x'+str(nao))
    with open('config/geom.txt', 'w') as geomdata:
        geomdata.write('')
        geom = geomdata.write(str(usar)+'x'+str(nao))
    geomdata.close()

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
    aguardaResposta = mb.askyesno(parent=janela, title='Writer Classic - Exit now?', message='You must reopen Writer to apply the changes!\nRestart now?')
    if aguardaResposta:
        janela.destroy()

def mudaIdioma(idioma, raiz):
    with open('config/lang.txt', 'w') as deleteThat:
        deleteThat.write('')
        deleteThat.write(idioma)
    kkkkSemRiso = mb.askyesno(parent=raiz, title='Writer Classic - Exit now?', message='You must reopen Writer to apply the changes!\nRestart now?')
    if kkkkSemRiso:
        raiz.destroy()

def formata_tudo(raiz):
    pois = mb.askyesno(title='Writer Classic - Delete data', message="Are you sure you want to delete Writer Classic's data?")
    if pois:
        ficheiro = dlg.askopenfilename(parent=raiz, filetypes = [(dd[1], '*.txt'), (dd[2], '*.html'), ('Python Script', '*.py'), ('JavaScript File', '*.js')])
        fich_teste = open(ficheiro, 'r')
        fich_test = fich_teste.read()
        if len(fich_test) != 0:
            fich_saida = open(ficheiro, 'w')
            fich_saida.write('')
            fich_saida.close()
        else:
            mb.showinfo(title=dd[36], message=dd[35])
            fich_teste.close()

def new_window():
    newWindow = Toplevel(janela)
    #Abrir os ficheiros de configuração
    with open('config/lang.txt', 'r') as langset:
        thisLang = langset.read()

    with open('data/'+str(thisLang)+'.txt', 'r', encoding='utf-8') as myLang2:
        myLang = myLang2.read()
        dd = myLang.split('//')

    with open('config/menu.txt', 'r', encoding='utf-8') as menuColor:
        mBg = menuColor.read()

    with open('config/mfg.txt', 'r', encoding='utf-8') as menuFg:
        mFg = menuFg.read()

    with open('config/menu.txt', 'r', encoding='utf-8') as corLeitura:
        corMenu = corLeitura.read()

    with open('config/mfg.txt', 'r', encoding='utf-8') as corFgLer:
        colorFg = corFgLer.read()

    #Configurar o texto e a newWindow
    newWindow.title(dd[38])

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

    #Fechar os ficheiros
    cbg.close()
    fgcnf.close()
    gbg.close()
    ccc.close()
    langset.close()

    newWindow.mainloop()

def website():
    ourMainWebsite = "https://sites.google.com/view/megati"

    webbrowser.open(ourMainWebsite, 2)

def repo():
    ourRepo = "https://github.com/MegaInformatica2022/WriterClassic/"

    webbrowser.open(ourRepo, 2)

def relogio():
    relog = Toplevel(janela)
    #Abrir os ficheiros de configuração

    #Configurar o texto e a newWindow
    relog.title(dd[39])

    texto = Label(relog)
    dias = Label(relog)

    texto.configure(text=datetime.datetime.now())
    dias.configure(text='Clock plugin by pythonPYhelper')
    texto.configure(
        font=(100)
        )

    dias.configure(
        font=(11)
        )

    relog.geometry('275x65')

    texto.pack()
    dias.pack()

    relog.mainloop()

def abrir(raiz):
    fich = dlg.askopenfilename(parent=raiz, filetypes=[('Text files', '*.txt'), ('HTML Files', '*.html'), ('Python Script', '*.py'), ('Java Source Code', '*.java'), ('Javascript File', '*.js')])
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
        mb.showinfo(title=dd[36], message=dd[35])
        fich_entrada = open(fich,'a')
        fich_ent2.close()

def salvar(raiz,texto):
    dados = texto.get('0.0', END)
    ficheiro = dlg.asksaveasfilename(parent=raiz, filetypes=[('Text files', '*.txt'), ('HTML Files', '*.html'), ('Python Script', '*.py'), ('Java Source Code', '*.java'), ('Javascript File', '*.js')])
    fich_saida = open(ficheiro, 'w')
    fich_saida.write(dados)
    fich_saida.close()

def salvarA(raiz, texto):
    dados = texto.get('0.0', END)
    ficheiro = dlg.asksaveasfilename(parent=raiz, filetypes=[('Text files', '*.txt'), ('HTML Files', '*.html'), ('Python Script', '*.py'), ('Java Source Code', '*.java'), ('Javascript File', '*.js')])
    fich_saida = open(ficheiro, 'a')
    fich_saida.write(dados)
    fich_saida.close()

def formatar(raiz):
    pois = mb.askyesno(title=dd[5], message=dd[6])
    if pois:
        ficheiro = dlg.askopenfilename(parent=raiz, filetypes = [(dd[1], '*.txt'), (dd[2], '*.html'), ('Python Script', '*.py'), ('JavaScript File', '*.js')])
        fich_teste = open(ficheiro, 'r')
        fich_test = fich_teste.read()
        if len(fich_test) != 0:
            fich_saida = open(ficheiro, 'w')
            fich_saida.write('')
            fich_saida.close()
        else:
            mb.showinfo(title=dd[36], message=dd[35])
            fich_teste.close()

def sair(raiz):
    confirm = mb.askyesno(title=dd[7], message=dd[8])
    if confirm:
        raiz.destroy()

def sair2(window):
    window.destroy()

def ajuda(thing1,mode):
    ourWebsite = "https://sites.google.com/view/megati/writer-o-projeto/ajuda"

    webbrowser.open(ourWebsite, 2)

def sobre(thing2, thing3):
    with open(thing2, thing3, encoding='utf-8') as about_d:
        about_data = about_d.read()
    mb.showinfo(title=dd[10], message=about_data)
    about_d.close()

'''def sobreisto(thing4):
    with open(thing4, 'r', encoding='utf-8') as about_d:
        about_data = about_d.read()
    mb.showinfo(title=dd[10], message=about_data)
    about_d.close()'''

janela.bind('<space>s', lambda a:
    salvarA(janela, texto))

janela.bind('<space>o', lambda b:
    abrir(janela))

janela.bind('<space>z', lambda c:
    salvar(janela, texto))

janela.bind('<space>w', lambda d:
    sair(janela))

janela.bind('<space>2', lambda e:
    sobre('data/about.txt', 'r'))

janela.bind('<space>1', lambda f:
    ajuda('data/help.txt', 'r'))

janela.bind('<space>d', lambda g:
    mudacor('black', 'white', 'white', 'dark grey', 'black'))

janela.bind('<space>l', lambda h:
    mudacor('white', 'black', 'black', 'black', 'white'))

janela.bind('<space>g', lambda j:
    janelageometrica1(janela,600,400))

janela.bind('<space>3', lambda k:
    formatar(janela))

janela.bind('<space>n', lambda l:
    relogio())

if __name__ == '__main__':
    barra_menu = Menu(janela)
    barra_menu.configure(background=mBg, foreground=mFg)
    ficheiro_menu = Menu(barra_menu)
    ficheiro_menu.add_command(label=dd[11], command=lambda:
        abrir(janela))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=dd[13], command=lambda:
        salvarA(janela, texto))
    ficheiro_menu.add_command(label = dd[12], command=lambda:
        salvar(janela,texto))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=dd[14], command=lambda:
        formatar(janela))
    ficheiro_menu.add_separator()
    ficheiro_menu.add_command(label=dd[15], command=lambda:
        sair(janela))
    
    editar_menu = Menu(barra_menu)
    editar_menu.add_command(label=dd[16], command=lambda:
        sobre('data/about.txt', 'r'))
    editar_menu.add_command(label=dd[17], command=lambda:
        ajuda('data/help.txt', 'r'))
    editar_menu.add_separator()
    editar_menu.add_command(label=dd[40], command=website)
    editar_menu.add_command(label=dd[41], command=repo)
    
    ver_menu = Menu(barra_menu)
    ver_1_m = Menu(ver_menu)
    ver_2_m = Menu(ver_menu)
    ver_3_m = Menu(ver_1_m)
    ver_5_m = Menu(ver_menu)
    ver_4_m = Menu(ver_5_m)
    ver_7_m = Menu(ver_5_m)
    b_m = Menu(barra_menu)
    
    b_m.add_command(label=dd[38], command=new_window)
    b_m.add_command(label=dd[39], command=relogio)
    
    a_m = Menu(barra_menu)
    a_m.add_command(label='English (UK)', command=lambda:
        mudaIdioma('en', janela))
    a_m.add_command(label='Português (Brasil)', command=lambda:
        mudaIdioma('br', janela))
    a_m.add_command(label='Português (Portugal)', command=lambda:
        mudaIdioma('pt', janela))
    
    ver_4_m.add_command(label=dd[18], command=lambda:
        mudacor('white', 'black', 'black', 'black', 'white'))
    ver_4_m.add_command(label=dd[19], command=lambda:
        mudacor('black', 'white', 'white', 'dark grey', 'black'))
    ver_4_m.add_separator()
    ver_4_m.add_command(label=dd[21], command=lambda:
        mudacor('grey', 'black', 'black', 'black', 'white'))
    
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
    ver_7_m.add_command(label='Yellow Powershell', command=lambda:
        mudacor('dark blue', 'yellow', 'yellow', '#020421', '#faf74d'))
    ver_7_m.add_command(label='Light Wizard', command=lambda:
        mudacor('purple', 'light yellow', 'light yellow', '#290340', '#edecaf'))
    ver_7_m.add_command(label='Dark Forest', command=lambda:
        mudacor('#0e2414', '#c0db7b', '#c0db7b', '#040d07', '#ccf0c5'))
    ver_7_m.add_command(label='Christmas Night', command=lambda:
       mudacor('#020421', '#a5a9e8', '#a5a9e8', '#020312', '#cbcef2'))
    ver_7_m.add_command(label='Silent Night', command=lambda:
        mudacor('#020421','pink', 'pink', '#020312', '#ebd1ed'))
    
    ver_2_m.add_command(label=dd[23],command=lambda:
        janelageometrica1(janela,600,400))
    ver_2_m.add_separator()
    ver_2_m.add_command(label='200x100',command=lambda:
        janelageometrica1(janela,200,100))
    ver_2_m.add_command(label='400x200',command=lambda:
        janelageometrica1(janela,400,200))
    ver_2_m.add_command(label='600x400',command=lambda:
        janelageometrica1(janela,600,400))
    ver_2_m.add_command(label='800x600',command=lambda:
        janelageometrica1(janela,800,600))
    ver_2_m.add_command(label='1000x800',command=lambda:
        janelageometrica1(janela,1000,800))
    ver_2_m.add_separator()
    ver_2_m.add_command(label='100x200',command=lambda:
        janelageometrica1(janela,100,200))
    ver_2_m.add_command(label='200x400',command=lambda:
        janelageometrica1(janela,200,400))
    ver_2_m.add_command(label='400x600',command=lambda:
        janelageometrica1(janela,400,600))
    ver_2_m.add_command(label='600x800',command=lambda:
        janelageometrica1(janela,600,800))
    ver_2_m.add_command(label='800x1000',command=lambda:
        janelageometrica1(janela,800,1000))
    ver_2_m.add_separator()
    ver_2_m.add_command(label='100x100',command=lambda:
        janelageometrica1(janela,100,100))
    ver_2_m.add_command(label='200x200',command=lambda:
        janelageometrica1(janela,200,200))
    ver_2_m.add_command(label='300x300',command=lambda:
        janelageometrica1(janela,300,300))
    ver_2_m.add_command(label='400x400',command=lambda:
        janelageometrica1(janela,400,400))
    ver_2_m.add_command(label='500x500',command=lambda:
        janelageometrica1(janela,500,500))
    ver_2_m.add_command(label='600x600',command=lambda:
        janelageometrica1(janela,600,600))
    ver_2_m.add_command(label='700x700',command=lambda:
        janelageometrica1(janela,700,700))
    ver_2_m.add_command(label='800x800',command=lambda:
        janelageometrica1(janela,800,800))
    ver_2_m.add_command(label='900x900',command=lambda:
        janelageometrica1(janela,900,900))
    ver_2_m.add_command(label='1000x1000',command=lambda:
        janelageometrica1(janela,1000,1000))

    ficheiro_menu.configure(background=corMenu, foreground=colorFg)
    editar_menu.configure(background=corMenu, foreground=colorFg)
    ver_menu.configure(background=corMenu, foreground=colorFg)
    ver_1_m.configure(background=corMenu, foreground=colorFg)
    ver_2_m.configure(background=corMenu, foreground=colorFg)
    ver_3_m.configure(background=corMenu, foreground=colorFg)
    ver_4_m.configure(background=corMenu, foreground=colorFg)
    ver_5_m.configure(background=corMenu, foreground=colorFg)
    ver_7_m.configure(background=corMenu, foreground=colorFg)
    a_m.configure(background=corMenu, foreground=colorFg)
    b_m.configure(background=corMenu, foreground=colorFg)

'''    menu2 = Menu(novidade)
    menu2.configure(background=mBg, foreground=mFg)

menu2.add_command(label=dd[11], command=lambda:
    abrir(novidade))
menu2.add_command(label=dd[13], command=lambda:
    salvarA(novidade))
menu2.add_command(label=dd[12], command=lambda:
    salvar(novidade))'''

barra_menu.add_cascade(label=dd[24],menu=ficheiro_menu)
barra_menu.add_cascade(label=dd[25],menu=ver_menu)
ver_menu.add_cascade(label=dd[26], menu=ver_5_m)
ver_5_m.add_cascade(label=dd[27], menu=ver_4_m)
ver_5_m.add_cascade(label=dd[29], menu=ver_7_m)
ver_menu.add_cascade(label=dd[30], menu=ver_2_m)
barra_menu.add_cascade(label='Plugins', menu=b_m)
barra_menu.add_cascade(label=dd[31], menu=a_m)
barra_menu.add_cascade(label=dd[32], menu=editar_menu)

janela.configure(menu=barra_menu)
'''novidade.configure(menu=menu2)'''
janela.mainloop()
