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

    def imprimir(self):
        atual = self.head
        s = ""
        while atual != None:   
             s = s + " " + str(atual.getData())
             atual = atual.getNext() # atual = atual.next
        print(s[1:])


def addInicio(lista,item):
    node = Node(item)
    node.setNext(lista.head)
    lista.head = node

'''
def buscar(lista, item):
    atual = lista.head
    while atual is not None:
        if atual.getData() == item:
            return item
        atual = atual.getNext()
    return None

'''
    
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

l = UnorderedList()
addInicio(l,1)
addInicio(l,2)
addInicio(l,3)
buscar(l,1)