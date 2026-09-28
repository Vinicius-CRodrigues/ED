class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # Insere no início da lista (O(n))
        self.items.insert(0, item)

    def dequeue(self):
        # Remove do final da lista (O(1))
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        for i in range(self.size()):
            print(f"{self.items[self.size() - i - 1]}", end=' ')
        print() # Quebra de linha ao final


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        for i in range(self.size()):
            # Imprime do topo para a base
            print(f"{self.items[self.size() - i - 1]}", end=' ')
        print()


class Cafeteria:
    def __init__(self):
        self.alunos = Queue()
        self.lanche = Stack()

def serve_almoco(self):
        cont_falhas = 0
        
        while not self.alunos.isEmpty() and cont_falhas < self.alunos.size():
            primeiro_aluno = self.alunos.dequeue()
            lanche_topo = self.lanche.peek()
            
            if primeiro_aluno == lanche_topo:
                self.lanche.pop()
                cont_falhas = 0
            else:
                self.alunos.enqueue(primeiro_aluno)
                cont_falhas += 1
        
        print(self.alunos.size())