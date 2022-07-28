import requests
import json
import qrcode
from tkinter import *
from TF_Classes import Sistema

#04324565000185 - Linha Livre 
#06990590000123 - Google
#83011247002346 - Tirol
#02290482000197 - Suq
#03489027000188 - Santa Rita
#82640558000104 - Karsten
#02314041000188 - IguaSport

#Cadastrar
def funcCadastrar():
    entrada = str(cnpj.get())
    
    if len(lista) == 0 :
        user = Sistema()
        lista.append(user)
        user.cadastrar(entrada)
    
    else:
        igual = False
        for i in lista:
            if i.GetCNPJ() == entrada :
                igual = True
        
        if (igual == True) :
            texto = 'Cadastro Já Realizado'
           
            #Criando Janela de mensagem do Pesquisar
            Janela = Tk()
            Janela.title('Cadastrar')
            Janela.geometry('350x150') #A largura deve ser ajustada com o texto
                    
            Texto = Label(Janela, text = '', padx = 100, pady = 25)
            Texto.grid(column = 0, row = 0)

            Texto['text'] = texto

            Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
            Botao.grid(column = 0, row = 1)
                    
            Janela.mainloop()
            
        else:
            user = Sistema()
            lista.append(user)
            user.cadastrar(entrada)

#Pesquisar
def funcPesquisar():
    
    if(len(lista) > 0):
        entrada = str(cnpj.get())
        pesquisado = False
        
        for user in lista:
            if(user.cadastro == True):
                if user.GetCNPJ() == entrada:
                    pesquisado = True
                    user.pesquisar()
        
        if(pesquisado == False):    
            texto = 'Cadastro Não Encontrado'
           
            #Criando Janela de mensagem do Pesquisar
            Janela = Tk()
            Janela.title('Pesquisar')
            Janela.geometry('400x150') #A largura deve ser ajustada com o texto
                    
            Texto = Label(Janela, text = '', padx = 100, pady = 25)
            Texto.grid(column = 0, row = 0)

            Texto['text'] = texto

            Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
            Botao.grid(column = 0, row = 1)
                    
            Janela.mainloop()

#QRCode
def funcQrcode():
    if(len(lista) > 0):
        entrada = str(cnpj.get())
        
        for user in lista:
            if(user.cadastro == True):
                if user.GetCNPJ() == entrada:
                    user.criarqrcode()
            else:
                
                texto = 'Cadastro Não Encontrado'
           
                #Criando Janela de mensagem do QR Code
                Janela = Tk()
                Janela.title('QR Code')
                Janela.geometry('400x150') #A largura deve ser ajustada com o texto
                    
                Texto = Label(Janela, text = '', padx = 100, pady = 25)
                Texto.grid(column = 0, row = 0)

                Texto['text'] = texto

                Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
                Botao.grid(column = 0, row = 1)
                    
                Janela.mainloop()

#Deletar
def funcDeletar():
    if(len(lista) > 0):
        entrada = str(cnpj.get())
        
        deletado = False
        
        texto = ''
        
        for pos, user in enumerate(lista):
            if user.GetCNPJ() == entrada:
                lista.pop(pos)
                deletado = True
                
        if deletado == True:
            
            #Texto da Janela do Deletar
            texto = "Cadastro Deletado Com Sucesso"
        else:
            
            #Texto da Janela do Deletar
            texto = "Cadastro Não Encontrado"
    
        #Criando Janela de mensagem do Deletar
        Janela = Tk()
        Janela.title('Deletar')
        Janela.geometry('400x150') #A largura deve ser ajustada com o texto
            
        Texto = Label(Janela, text = '', padx = 100, pady = 25)
        Texto.grid(column = 0, row = 0)

        Texto['text'] = texto

        Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
        Botao.grid(column = 0, row = 1)
            
        Janela.mainloop()
    
#Listar
def funcListar():

    if(len(lista) > 0):
        c = ''
        for i in lista:
            if(i.cadastro == True):
                c = c + '\n' + i.GetCNPJ() + ' ' + '-' + ' ' + i.GetNome()
        texto = c
    
        #Criando Janela de mensagem do Listar
        Janela = Tk()
        Janela.title('Listar')
        Janela.geometry('600x300') #A largura deve ser ajustada com o texto
            
        Texto = Label(Janela, text = '', padx = 100, pady = 25)
        Texto.grid(column = 0, row = 0)

        Texto['text'] = texto

        Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
        Botao.grid(column = 0, row = 1)
            
        Janela.mainloop()

#Declaração de Variáveis
lista = []

#Janela Principal

Janela01 = Tk()
Janela01.title('Menu Principal')
Janela01.geometry('350x350')

cnpj = StringVar()
Entrada = Entry(Janela01, justify = CENTER, textvariable = cnpj)
Entrada.grid(column = 0, row = 0, padx = 100, pady = 25)
    
Botao01 = Button(Janela01, text = '     Cadastrar CNPJ     ', command = funcCadastrar, bg = 'light blue', padx = 35, pady = 5)
Botao01.grid(column = 0, row = 1)


Botao02 = Button(Janela01, text = '   Pesquisar Cadastro   ', command = funcPesquisar, bg = 'light blue', padx = 30, pady = 5 )
Botao02.grid(column = 0, row = 2)


Botao03 = Button(Janela01, text = '     Baixar QR Code     ', command = funcQrcode, bg = 'light blue', padx = 33, pady = 5  )
Botao03.grid(column = 0, row = 3)

Botao04 = Button(Janela01, text = '    Deletar Cadastro    ', command = funcDeletar, bg = 'light blue', padx = 33, pady = 5  )
Botao04.grid(column = 0, row = 4)


Botao05 = Button(Janela01, text = 'Listar CNPJs Cadastrados', command = funcListar, bg = 'light blue', padx = 23, pady = 5  )
Botao05.grid(column = 0, row = 5)


Botao06 = Button(Janela01, text = '          Sair          ', command = Janela01.destroy, bg = 'light blue', padx = 20, pady = 5  )
Botao06.grid(column = 0, row = 6)

Janela01.mainloop()