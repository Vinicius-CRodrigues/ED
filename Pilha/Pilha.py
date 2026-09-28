class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def seeTop(self):
        return self.items[-1]
    


def findDiamond(entrada):
    pilha = stack()
    cont = 0

    for i in entrada:
        if i == '<':
            pilha.push(i)
        elif not pilha.isEmpty() and i == '>' and pilha.pop() == '<':
            cont += 1
    
    return cont




print (findDiamond('.<.<..<...>...>....>....<.......<.>'))

'''
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

'''


