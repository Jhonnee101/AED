from classes import Carrinho, Produto

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