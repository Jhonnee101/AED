class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} está falando")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse} está comprando")    


class Aluno(Pessoa):
    def estudando(self):
        print(f"{self.nomeclasse} Está estudando")


c1 = Cliente("Luiz", 23)
c1.falar()
c1.comprar()


a1 = Aluno("Maria", 23)
a1.falar()
a1.estudando()