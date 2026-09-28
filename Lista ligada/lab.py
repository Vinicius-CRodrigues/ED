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

L = UnorderedList()
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
print(f'Lista antes: {L}')
inverterLista(L)
print(f'Lista depois: {L}')
