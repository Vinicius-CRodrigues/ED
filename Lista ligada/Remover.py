class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
       return self.head == None

    def __str__(self):
       s = "["
       atual = self.head
       while atual != None:
          s = s + str(atual.getData()) +","
          atual = atual.getNext()
       if s[-1] == ",":
          s = s[0:-1]
       s = s + "]"
       return s
    def append(self,item):
        novo = Node(item)
        if self.isEmpty():
           self.head = novo
        else:
           u = self.head
           while u.getNext() != None:
                 u = u.getNext()
           u.setNext(novo)

def inverterLista(L : UnorderedList):
    anterior = None 
    atual = L.head
    while atual != None:
        proximo = atual.getNext()
        atual.setNext(anterior)
        anterior = atual
        atual = proximo
    L.head = anterior

    return L

def buscar(lista, item):
    atual = lista.head
    anterior = None
    
    while atual is not None:
        if atual.getData() == item:
            if anterior is None:
                return item
            anterior.setNext(atual.getNext())
            atual.setNext(lista.head)
            lista.head = atual
            return item
        
        anterior = atual
        atual = atual.getNext()
    return None

def remove(self, item):
    atual = self.head
    anterior = None
    encontrado = False

    # 1. Passo: Buscar o elemento na lista mantendo o ponteiro anterior
    while atual != None and not encontrado:
        if atual.getData() == item:
            encontrado = True
        else:
            anterior = atual          # O anterior avança para onde o atual estava
            atual = atual.getNext()   # O atual avança para o próximo nó

    # Se o elemento não foi encontrado, o método termina sem fazer nada
    if not encontrado:
        return False # Ou apenas 'return', dependendo do que o professor pedir

    # 2. Passo: Ajustar os ponteiros para remover o nó
    if anterior == None:
        # CASO DE BORDA: O item estava no primeiro nó (head)
        self.head = atual.getNext()
    else:
        # CASO GERAL: O item estava no meio ou no fim da lista
        anterior.setNext(atual.getNext())
        
    return True