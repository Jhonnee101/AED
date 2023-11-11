class Carrinho:
    def __init__(self):
        self.produtos = []

    def inserir(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    
carrinho = Carrinho()
p1 = Produto('Arroz', 6)
p2 = Produto('Macarrao', 4)
p3 = Produto('Uva', 5)
p4 = Produto('Batata', 8)

carrinho.inserir(p1)
carrinho.inserir(p2)
carrinho.inserir(p3)
carrinho.inserir(p4)

carrinho.listar()
print(carrinho.soma_total())