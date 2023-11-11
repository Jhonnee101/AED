class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


    def __del__(self):
        print(f"{self.nome} FOI APAGADO")


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f"{self.cidade} FOI APAGADO")


cliente1 = Cliente("Luiz", 22)
cliente1.inserir_endereco("Serra Talhada", "PE")
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()
cliente2 = Cliente("Joao", 22)
cliente2.inserir_endereco("Afogados", "PE")
print(cliente2.nome)
cliente2.lista_enderecos()
print()
cliente3 = Cliente("Maria", 22)
cliente3.inserir_endereco("Tabira", "PE")
print(cliente3.nome)
cliente3.lista_enderecos()


print("########################################")