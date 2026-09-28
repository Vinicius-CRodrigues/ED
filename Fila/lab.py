# Implementação de filas com pilhas.

class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
class Fila_comPilhas:
    
    def __init__(self):
        self.pilha1 = stack()
        self.pilha2 = stack()
    


        

fila = Fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
fila.imprime()
print('------------------------------')
#  fila = Fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
print('dequeue - '+str(fila.dequeue()))
fila.enqueue(6)
print('dequeue - '+str(fila.dequeue()))
print('dequeue - '+str(fila.dequeue()))
fila.imprime()