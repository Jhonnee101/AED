class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo

        def __str__(self):
            return str(self.valor)

    def __init__(self):
        self.__cabeca = None
        self.__cauda = None
        self.__quantidade = 0

    def __len__(self):
        return self.__quantidade

    def __str__(self):
        saida = '['
        atual = self.__cabeca
        while atual is not None:
            saida += str(atual.valor)
            if atual.proximo is not None:
                saida += ', '
            atual = atual.proximo
        saida += ']'

        return saida

    def __iter__(self):
        atual = self.__cabeca
        while atual is not None:
            yield atual.valor  # lazy evaluating
            atual = atual.proximo

    def __getitem__(self, posicao):
        # se for do tipo slice, vamos retornar o slice (fatia)
        if isinstance(posicao, slice):
            passo = posicao.step if posicao.step is not None else 1

            if passo == 0:
                raise ValueError('O passo não pode ser zero')

            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0
                fim = posicao.stop if posicao.stop is not None else len(self)
            else:
                inicio = posicao.start if posicao.start is not None else len(self) - 1
                fim = posicao.stop if posicao.stop is not None else -1

            if inicio < 0:
                inicio += len(self)

            if fim < 0 and posicao.stop is not None:
                fim += len(self)

            fatia = Lista()
            if passo > 0:
                # usar lazy evaluating quando a fatia está em ordem crescente
                it = iter(self)
                i = 0
                while i < fim:
                    valor = next(it)
                    if i >= inicio:
                        fatia.inserir_no_fim(valor)
                    i += 1
            else:
                # criar uma fatia em ordem decrescente, não podemos usar o lazy evaluating
                # só com uma lista duplamente encadeada...
                # então vamos usar o __getitem__ para acessar os elementos
                i = inicio
                while i > fim:
                    fatia.inserir_no_fim(self[i])
                    i += passo

            return fatia

        if posicao < 0:
            posicao += len(self)

        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição inválida')

        i = 0  # índice do elemento atual
        atual = self.__cabeca
        while atual is not None and i < posicao:
            atual = atual.proximo
            i += 1

        return atual.valor

    def __setitem__(self, posicao, valor):
        if posicao < 0:
            posicao += len(self)

        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição inválida')

        i = 0
        atual = self.__cabeca
        while atual is not None and i < posicao:
            atual = atual.proximo
            i += 1

        atual.valor = valor

    def inserir_no_fim(self, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        # quando a lista está vazia
        if self.__cabeca is None:
            self.__cabeca = novo
            self.__cauda = novo
            return

        # quando a lista tem pelo menos um elemento
        self.__cauda.proximo = novo
        self.__cauda = novo

    def __delitem__(self, posicao):
        # falta apagar via fatia/slice
        if posicao < 0:
            posicao += len(self)

        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição inválida')

        self.__quantidade -= 1

        # quando a lista tem apenas um elemento
        if self.__cabeca == self.__cauda:
            self.__cabeca = None
            self.__cauda = None
            return

        # quando quer remover a cabeça (primeiro elemento)
        if posicao == 0:
            self.__cabeca = self.__cabeca.proximo
            return

        # para todos os outros elementos...
        # buscar o elemento anterior do qual eu quero apagar
        i = 0
        atual = self.__cabeca
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1

        # se for remover o último elemento, atualizar o ponteiro cauda
        if atual.proximo == self.__cauda:
            self.__cauda = atual

        atual.proximo = atual.proximo.proximo

    def inserir(self, posicao, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        # quando a lista está vazia
        if self.__cabeca is None:
            self.__cabeca = novo
            self.__cauda = novo
            return

        # quando quer inserir na cabeça (na primeira posição)
        if posicao <= 0:
            novo.proximo = self.__cabeca
            self.__cabeca = novo
            return

        # quando quer inserir em qualquer posição
        # queremos encontrar o nó anterior
        i = 0
        atual = self.__cabeca
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1

        if atual.proximo is None:
            self.__cauda = novo

        # atualizando os ponteiros
        novo.proximo = atual.proximo
        atual.proximo = novo

    def __reversed__(self):
        return self[::-1]

    def inverter(self):
        copia = self.copiar()
        self.clear()
        for elemento in copia:
            self.inserir(0, elemento)

    def copiar(self):
        return self[:]

    def contar(self, valor):
        contador = 0
        for elemento in self:
            if elemento == valor:
                contador += 1

        return contador

    def indice(self, valor):
        for i, elemento in enumerate(self):
            if elemento == valor:
                return i

        raise ValueError(f'{valor} não está na lista')

    def clear(self):
        self.__cabeca = None
        self.__cauda = None
        self.__quantidade = 0

    def pop(self, posicao=-1):
        if len(self) == 0:
            raise IndexError('A lista está vazia')

        valor = self[posicao]
        del self[posicao]

        return valor

    def remover(self, valor):
        posicao = self.indice(valor)
        del self[posicao]

    def estender(self, iteravel):
        for elemento in iteravel:
            self.inserir_no_fim(elemento)

            
    def delete_slice(self, start, end):
        if start > end:
            return
        atual = self.__cabeca
        count = 0
        antigo = None
        while atual and count <= end:
            if count == start:
                primeiro_no = atual
            antigo = atual
            atual = atual.proximo
            count += 1
        atual = primeiro_no
        for _ in range(start, end + 1):
            proximo_no = atual.proximo
            atual.proximo = None
            atual = proximo_no
        if antigo is not None:
            antigo.proximo = atual
        else:
            self.__cabeca = atual


pessoas= Lista()
pessoas.inserir(0, 'João')
pessoas.inserir(1, 'Maria')
pessoas.inserir(2, 'José')
pessoas.inserir(3, 'Ana')
pessoas.inserir(4, 'Carlos')
pessoas.inserir(5, 'Ana')

print(len(pessoas))

# print(pessoas[1:3])
# for pessoa in pessoas[::-1]:
#     print(pessoa)

# for pessoa in pessoas:
#     print(pessoa)

print(pessoas)
pessoas[2] = 'Josefina'
print(pessoas)

animais = Lista()
animais.inserir_no_fim('Cachorro')
animais.inserir(0, 'Gato')
animais.inserir(1, 'Papagaio')
print(animais)

pessoas.estender(animais)
print(pessoas)
#pessoas.inverter()
print(pessoas)
pessoas.delete_slice(1, 3)
print(pessoas)