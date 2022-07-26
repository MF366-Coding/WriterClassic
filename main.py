'''

Writer

Made in Python 3

Original idea by: Mega Informática
Developed by: Mega Informática

'''

#Importar os módulos necessários
from tkinter import *
import tkinter.filedialog as dlg
import tkinter.messagebox as mb
import webbrowser

#Criar a janela
janela = Tk()

#Abrir os ficheiros de configuração
with open('config/lang.txt', 'r') as langset:
    thisLang = langset.read()

with open('data/'+str(thisLang)+'.txt', 'r', encoding='utf-8') as myLang2:
    myLang = myLang2.read()
    dd = myLang.split('//')

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


def mudacor(cor, fgcor, cc):
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

def new_window():
    newWindow = Toplevel(janela)
    #Abrir os ficheiros de configuração
    with open('config/lang.txt', 'r') as langset:
        thisLang = langset.read()

    with open('data/'+str(thisLang)+'.txt', 'r', encoding='utf-8') as myLang2:
        myLang = myLang2.read()
        dd = myLang.split('//')

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
    ourRepo = "https://github.com/MegaInformatica2022/Writer/"

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

def mudaIdioma(idioma, raiz):
    with open('config/lang.txt', 'w') as deleteThat:
        deleteThat.write('')
        deleteThat.write(idioma)
    kkkkSemRiso = mb.askyesno(parent=raiz, title='Writer 5.0.0 - Exit now?', message='You must reopen Writer to apply the changes!\nRestart now?')
    if kkkkSemRiso:
        raiz.destroy()

def formata(raiz):
    with open('config/lang.txt', 'w', encoding='utf-8') as a1:
        a1.write('en')
    with open('config/geom.txt', 'w', encoding='utf-8') as a2:
        a2.write('600x400')
    with open('config/fg.txt', 'w', encoding='utf-8') as a3:
        a3.write('#a5a9e8')
    with open('config/colour.txt', 'w', encoding='utf-8') as a4:
        a4.write('#020421')
    with open('config/ct.txt', 'w', encoding='utf-8') as a5:
        a5.write('#a5a9e8')
    kkkSemRiso = mb.askyesno(parent=raiz, title='Writer 5.0.0 - Exit now?', message='You must reopen Writer to apply the changes!\nRestart now?')
    if kkkSemRiso:
        raiz.destroy()

def abrir(raiz):
    fich = dlg.askopenfilename(parent=raiz, filetypes=[('Text files', '*.txt'), ('HTML Files', '*.html'), ('Python Script', '*.py'), ('Java Source Code', '*.java'), ('Javascript File', '*.js')])
    fich_ent2 = open(fich, 'r')
    resultado = fich_ent2.read()
    if len(resultado) > 0:
        mb.showinfo(title=dd[3], message=str(dd[4])+'\n\n'+str(resultado))
        fich_entrada = open(fich,'a')
        fich_ent2.close()
    else:
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
        fich_saida = open(ficheiro, 'w')
        fich_saida.write('')
        fich_saida.close()

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

def janelageometrica1(indicar,usar,nao):
    indicar.geometry(str(usar)+'x'+str(nao))
    with open('config/geom.txt', 'w') as geomdata:
        geom = geomdata.write(str(usar)+'x'+str(nao))
    geomdata.close()

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
    editar_menu.add_command(label=dd[37], command=website)
    editar_menu.add_command(label=dd[38], command=repo)
    ver_menu = Menu(barra_menu)
    ver_1_m = Menu(ver_menu)
    ver_2_m = Menu(ver_menu)
    ver_3_m = Menu(ver_1_m)
    ver_5_m = Menu(ver_menu)
    ver_4_m = Menu(ver_5_m)
    ver_6_m = Menu(ver_5_m)
    ver_7_m = Menu(ver_5_m)
    b_m = Menu(barra_menu)
    a_m = Menu(barra_menu)
    a_m.add_command(label='English (UK)', command=lambda:
        mudaIdioma('en', janela))
    a_m.add_command(label='Português (Brasil)', command=lambda:
        mudaIdioma('br', janela))
    a_m.add_command(label='Português (Portugal)', command=lambda:
        mudaIdioma('pt', janela))
    a_m.add_separator()
    a_m.add_command(label=dd[33], command=lambda:
        formata(janela))
    ver_4_m.add_command(label=dd[18], command=lambda:
        mudacor('white', 'black', 'black'))
    ver_4_m.add_command(label=dd[19], command=lambda:
        mudacor('black', 'white', 'white'))
    ver_4_m.add_separator()
    ver_4_m.add_command(label=dd[20], command=lambda:
        mudacor('light grey', 'black', 'black'))
    ver_4_m.add_command(label=dd[21], command=lambda:
        mudacor('dark grey', 'black', 'black'))
    ver_4_m.add_command(label=dd[22], command=lambda:
        mudacor('grey', 'black', 'black'))
    ver_6_m.add_command(label='Light Yellow', command=lambda:
        mudacor('light yellow', 'black', 'black'))
    ver_6_m.add_command(label='Magic', command=lambda:
        mudacor('purple', 'white', 'white'))
    ver_6_m.add_command(label='Through the Sky', command=lambda:
        mudacor('light blue', 'black', 'black'))
    ver_6_m.add_command(label='Light Green', command=lambda:
        mudacor('light green', 'black', 'black'))
    ver_7_m.add_command(label='Codetime', command=lambda:
        mudacor('black', 'green', 'green'))
    ver_7_m.add_command(label='Yellow Powershell', command=lambda:
        mudacor('dark blue', 'yellow', 'yellow'))
    ver_7_m.add_command(label='Light Wizard', command=lambda:
        mudacor('purple', 'light yellow', 'light yellow'))
    ver_7_m.add_command(label='Dark Forest', command=lambda:
        mudacor('#0e2414', '#c0db7b', '#c0db7b'))
    ver_7_m.add_command(label='Christmas Night', command=lambda:
       mudacor('#020421', '#a5a9e8', '#a5a9e8'))
    ver_7_m.add_command(label='Silent Night', command=lambda:
        mudacor('#020421','pink', 'pink'))
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
    b_m.add_command(label=dd[35], command=new_window)
    b_m.add_command(label=dd[36], command=relogio)

barra_menu.add_cascade(label=dd[24],menu=ficheiro_menu)
barra_menu.add_cascade(label=dd[25],menu=ver_menu)
ver_menu.add_cascade(label=dd[26], menu=ver_5_m)
ver_5_m.add_cascade(label=dd[27], menu=ver_4_m)
ver_5_m.add_cascade(label=dd[28], menu=ver_6_m)
ver_5_m.add_cascade(label=dd[29], menu=ver_7_m)
ver_menu.add_cascade(label=dd[30], menu=ver_2_m)
barra_menu.add_cascade(label='Plugins', menu=b_m)
barra_menu.add_cascade(label=dd[31], menu=a_m)
barra_menu.add_cascade(label=dd[32],menu=editar_menu)

janela.configure(menu=barra_menu)
janela.mainloop()
