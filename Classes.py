import requests
import json
import qrcode
from tkinter import *

#04324565000185 - Linha Livre 
#06990590000123 - Google
#83011247002346 - Tirol
#02290482000197 - Suq
#03489027000188 - Santa Rita
#82640558000104 - Karsten
#02314041000188 - IguaSport


class Sistema:
    
    #Construtor
    def __init__(self):
        self.nome = ''
        self.cnpj = ''
        self.situacao = ''
        self.abertura = ''
        self.telefone = ''
        self.logradouro = ''
        self.municipio = '' 
        self.cep = ''
        self.cadastro = False
       
    #Getters 
    def GetNome(self):
        return self.nome
    
    def GetCNPJ(self):
        return self.cnpj
    
    #Cadastro do usuário no sistema
    def cadastrar(self,cnpj):
        
        texto = ''
        
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
        response = requests.request("GET", url, params=querystring)
    
        resp = json.loads(response.text)
        
        if resp['status'] != 'ERROR':
            logradouro = str(f"{resp['logradouro']}, {resp['bairro']}")
            municipio = str(f"{resp['municipio']}, {resp['uf']}")
        
            self.nome = resp['nome']
            self.cnpj = cnpj
            self.situacao = resp['situacao']
            self.abertura = resp['abertura']
            self.telefone = resp['telefone']
            self.logradouro = logradouro
            self.municipio = municipio 
            self.cep = resp['cep']
            
            texto = 'Cadastro Realizado Com Sucesso'
            self.cadastro = True
        
        else:
            
            #Texto da Janela do Cadastrar
            texto = 'Cadastro Não Realizado'
        
        #Criando Janela de mensagem do Cadastrar
        Janela = Tk()
        Janela.title('Cadastrar')
        Janela.geometry('400x150') #A largura deve ser ajustada com o texto
            
        Texto = Label(Janela, text = '', padx = 100, pady = 25)
        Texto.grid(column = 0, row = 0)

        Texto['text'] = texto

        Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
        Botao.grid(column = 0, row = 1)
            
        Janela.mainloop()


    #Pesquisar cadastro de usuários
    def pesquisar(self):
        
        #Texto da Janela do Pesquisar
        texto = 'Nome: {}\nCNPJ: {}\nSituação Cadastral: {}\nData de Abertura: {}\nTelefone: {}\nEndereço: {}, {}\nCEP: {}'.format(self.nome, self.cnpj, self.situacao, self.abertura, self.telefone, self.logradouro, self.municipio, self.cep)
       
        #Criando Janela de mensagem do Pesquisar
        Janela = Tk()
        Janela.title('Pesquisar')
        Janela.geometry('600x300') #A largura deve ser ajustada com o texto
            
        Texto = Label(Janela, text = '', padx = 100, pady = 25)
        Texto.grid(column = 0, row = 0)

        Texto['text'] = texto

        Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
        Botao.grid(column = 0, row = 1)
            
        Janela.mainloop()
        
        
    #Criar QR Code do usuário    
    def criarqrcode(self):
        
        data = 'Nome: {}\nCNPJ: {}\nSituação Cadastral: {}\nData de Abertura: {}\nTelefone: {}\nEndereço: {}, {}\nCEP: {}'.format(self.nome, self.cnpj, self.situacao, self.abertura, self.telefone, self.logradouro, self.municipio, self.cep)
        img = qrcode.make(data)
        img.save('QRCode.png')
        
        #Texto da Janela do QR Code
        texto = 'Download Concluído'
       
        #Criando Janela de mensagem do QR Code
        Janela = Tk()
        Janela.title('QR Code')
        Janela.geometry('350x150') #A largura deve ser ajustada com o texto
            
        Texto = Label(Janela, text = '', padx = 100, pady = 25)
        Texto.grid(column = 0, row = 0)

        Texto['text'] = texto

        Botao = Button(Janela, text = 'Voltar', command = Janela.destroy, bg = 'light blue', padx = 20, pady = 5 )
        Botao.grid(column = 0, row = 1)
            
        Janela.mainloop()