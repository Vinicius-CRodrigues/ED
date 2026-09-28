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


    def enqueue(self, item):
        # O item sempre entra na pilha 1 (topo da pilha 1 é o fim da fila)
        self.pilha1.push(item)

    def dequeue(self):
        # Se a pilha 2 estiver vazia, transferimos tudo da pilha 1 para inverter a ordem
        if self.pilha2.isEmpty():
            while not self.pilha1.isEmpty():
                self.pilha2.push(self.pilha1.pop())
        
        # Se após a transferência a pilha 2 ainda estiver vazia, a fila está vazia
        if self.pilha2.isEmpty():
            return None
            
        return self.pilha2.pop()
    
    def imprime(self):
        p_aux = stack()
        
        while not self.pilha2.isEmpty():
            item = self.pilha2.pop()
            print(item)
            p_aux.push(item)
        
        while not p_aux.isEmpty():
            self.pilha2.push(p_aux.pop())
            
        p_inversora = stack()
        while not self.pilha1.isEmpty():
            p_inversora.push(self.pilha1.pop())
        
        while not p_inversora.isEmpty():
            item = p_inversora.pop()
            print(item)
            p_aux.push(item)
            
        while not p_aux.isEmpty():
            self.pilha1.push(p_aux.pop())

fila = Fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
fila.imprime()
print('------------------------------')

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