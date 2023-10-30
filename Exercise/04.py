from node import Node
#sequencial = []
#sequencial.append(1)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            #Inserir quando a lista ja possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #Primeira insercao
            self.head = Node(elem)
        self._size +=1

    def __len__(self):
        #Retorna o tamanho da lista
        return self._size
    
    def get(self, index):
        pass

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        #a = lista[5]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
            
        if pointer:
            return pointer.data
        
        raise IndexError("list index out of range")
        

    def __setitem__(self, index, elem):
        #a = lista[5]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
            
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
        
    def index(self,elem):
        #Retorna o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            else:
                pointer = pointer.next
                i += 1
        raise ValueError(f'{elem} nao esta na lista')

lista = LinkedList()
lista.append(7)