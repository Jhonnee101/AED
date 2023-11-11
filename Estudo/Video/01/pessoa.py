class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
        if self.falando:
            print(f"{self.nome} nao pode comer falando")

        print(f"{self.nome} está comendo {alimento}")
        self.comendo = True


    def parar_de_comer(self):
        if not self.comendo:
            print(f"{self.nome} nao esta comendo")
            return
        print(f"{self.nome} parou de comer")
        self.comendo = False


    def falar(self, assunto):
        if self.comendo == True:
            print(f"{self.nome} nao pode falar comendo")
            return
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        
        print(f"{self.nome} está falando sobre {assunto}")
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f"{self.nome} nao esta falando")
            return
        
        print(f"{self.nome} parou de falar")
        self.falando = False


p1 = Pessoa('Luiz', 22)
p2 = Pessoa('Joao', 23) 

p1.comer("Banana")
p1.falar('POO')
p1.parar_de_comer()
p1.falar("POO")
p1.parar_de_falar()
p1.comer("Maca")
p1.falar("SI")