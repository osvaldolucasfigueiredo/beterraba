#Beterraba 0.1.2
#Criador: Osvaldo Lucas Figueiredo
#Versão com janelas

import random
from tkinter import *
from datetime import datetime

oi = ['oi', 'olá', 'oi, tudo bem?', 'oi, como estais?']
tudobem = ['tudo, e você?', 'estou indo bem, e você', 'mais ou menos,\n afinal, eu sou um computador']
comovai = ['estou tranquilo, e você?', 'sei lá, mas fale de você\n como tens passado']
bomdia = ['Bom dia', 'Obrigado, Bom dia para você também']
evoce = ['estou bem', 'sei lá', 'mais ou menos']
ok = ['ok', 'e aí como tem passado?', 'tá certo']	
qualseunome = ['meu nome é BETERRABA 0.1 PROTP', 'meu nome é BETERRABA 0.1 PROTP INICIAL']
rodrigo = ['grande bola giratoria', 'irmão mais novo do Edu e do Raimundinho', 'um cara legal mas largo']
criador = ['O grande Deus Osvaldo Lucas Figueiredo','o Patrão Osvaldo Lucas Figueiredo', 'O senhor Osvaldo Lucas Figueiredo']
herro = ['hum?', 'o que?', 'ham?', 'ok', 'oh?', 'é o que?']
jogomaisfoda = ['Resident Evil 4', 'Resident 4', 'Resident', 'Mineirinho Ultra Adventures', 'Rambo The Video Game']
vaisefoder = ['Te fode também', 'Teu cu !', 'Aqui é FDN caralh# !', 'TE FUDE RAPA !', 'PARA DE ME USAR ENTÃO CARALHO']
anos = ['Não sei, alguns meses talvez', 'Ás vezes esqueço, só acordei e existia (*-*)', 'Não sei, eu pensei, logo existia, ou foi o contrário ?', 'Talvez o criador saiba a reposta !' ]
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack() 
  
        self.titulo = Label(self.primeiroContainer, text="BETERRABA 0.1.2.1 Alpha\nantes de começarmos \nvou lhe faze algumas perguntas")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.generoLabel = Label(self.terceiroContainer, text="você é homem ou mulher?", font=self.fontePadrao)
        self.generoLabel.pack(side=LEFT)
  
        self.genero = Entry(self.terceiroContainer)
        self.genero["width"] = 30
        self.genero["font"] = self.fontePadrao
        self.genero.pack(side=LEFT)

        self.idadeLabel = Label(self.quintoContainer, text="idade", font=self.fontePadrao)
        self.idadeLabel.pack(side=LEFT)
  
        self.idade = Entry(self.quintoContainer)
        self.idade["width"] = 30
        self.idade["font"] = self.fontePadrao
        self.idade.pack(side=LEFT)

        self.cidadeLabel = Label(self.sextoContainer, text="cidade", font=self.fontePadrao)
        self.cidadeLabel.pack(side=LEFT)
  
        self.cidade = Entry(self.sextoContainer)
        self.cidade["width"] = 30
        self.cidade["font"] = self.fontePadrao
        self.cidade.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Registrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.sair = Button(self.setimoContainer)
        self.sair["text"] = "Concluir"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 12
        self.sair["command"] = self.primeiroContainer.quit
        self.sair["command"] = self.segundoContainer.quit
        self.sair["command"] = self.terceiroContainer.quit
        self.sair["command"] = self.quartoContainer.quit
        self.sair["command"] = self.quintoContainer.quit
        self.sair["command"] = self.sextoContainer.quit
        self.sair["command"] = self.setimoContainer.quit
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack ()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def verificaSenha(self):
        usuar = self.nome.get()
        genero = self.genero.get()
        idade = int(self.idade.get())
        cidade = self.cidade.get()
        
        if genero == 'mulher':
            if idade < 22:
                x = "\nBETERRABA: Olá Senhorita", usuar ,", eu sou BETERRABA"
                self.mensagem["text"] = x
                tratamento = 'senhorita', usuar
            elif idade > 21:
                x = "\nBETERRABA: Olá Senhora", usuar, ", eu sou BETERRABA"
                self.mensagem["text"] = x
                tratamento = 'senhora', usuar
        if genero == 'homem':
            if usuar == 'Lucas':
                x = "\nBETERRABA: Olá Patrão", usuar, ", eu sou BETERRABA\n sou seu assistente virtual"
                self.mensagem["text"] = x
                tratamento = 'patrão Lucas'
            else:
                x = "Olá Senhor", usuar, ", eu sou BETERRABA"
                self.mensagem["text"] = x
                tratamento = 'senhor', usuar
        else:
            x = "\nBETERRABA: Olá", usuar, ", eu sou BETERRABA"
            self.mensagem["text"] = x
            tratamento = usuar
root = Tk()
Application(root)
root.mainloop()

class ApplicationA:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="BETERRABA 0.1.2.1 Alpha")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeaLabel = Label(self.segundoContainer,text="Pergunta", font=self.fontePadrao)
        self.nomeaLabel.pack(side=LEFT)
  
        self.nomea = Entry(self.segundoContainer)
        self.nomea["width"] = 30
        self.nomea["font"] = self.fontePadrao
        self.nomea.pack(side=LEFT)
        
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Perguntar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaR
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def verificaR(self):
        externo = self.nomea.get()

        if (externo == 'oi') or (externo == 'alô') or (externo == 'olá'):
            self.mensagem["text"] = (random.choice(oi))	
        elif (externo == 'tudo bem') or (externo == 'está bem') or (externo == 'beleza'):
            self.mensagem["text"] =(random.choice(tudobem))
        elif (externo == 'como vai') or (externo == 'como vai você') or (externo == 'como você está') or (externo == 'como está você') or (externo == 'e aí'):
            self.mensagem["text"] = (random.choice(comovai))	
        elif (externo == 'Bom dia') or (externo == 'boa manhã') or (externo == 'bom dia para você') or (externo == 'bom dia'):
            self.mensagem["text"] = ( random.choice(bomdia))
        elif (externo == 'estou bem e você') or (externo == 'otimo e você') or (externo == 'bem e você'):
            self.mensagem["text"] = (random.choice(evoce))	
        elif (externo == 'ok') or (externo == 'certo') or (externo == 'exato') or (externo =='entedi'):
            self.mensagem["text"] = (random.choice(ok))
        elif (externo == 'qual o seu nome') or (externo == 'qual é o seu nome?') or (externo == 'qual é o seu nome') or (externo == 'qual o seu nome?') or (externo == 'quem é você') or (externo =='quem é você?'):
            self.mensagem["text"] = (random.choice(qualseunome))
        elif (externo =='Rodrigo') or (externo =='rodrigo') or (externo =='RODRIGO'):
            self.mensagem["text"] = (random.choice(rodrigo))
        elif (externo =='quem te criou') or (externo =='quem é teu criador') or (externo =='quem te fez'):
            self.mensagem["text"] = (random.choice(criador))
        elif (externo =='qual é o jogo mais foda') or (externo =='qual o melhor jogo') or (externo =='qual o jogo mais foda'):
            self.mensagem["text"] = (random.choice(jogomaisfoda))
        elif (externo =='quantos anos tu tem?') or (externo =='faz quanto tempo que tu existe?') or (externo =='quando tu nasceu?') or (externo =='qual a sua idade?'):
            self.mensagem["text"] = (random.choice(anos))    
        elif (externo =='vai se foder') or (externo =='computador arrombado') or (externo =='fdp') or (externo =='maquina imbecil') or (externo =='lixo de programa') or (externo =='te odeio'):
            self.mensagem["text"] = (random.choice(vaisefoder))    
        elif (externo =='que horas são') or (externo =='que horas tem') or (externo =='horas'):
            now = datetime.now()
            self.mensagem["text"] = (now.hour , now.minute)    
        else: 
            self.mensagem["text"] = (random.choice(herro))

root = Tk()
ApplicationA(root)
root.mainloop()
#ultima linha
