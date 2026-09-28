class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

N = int(input()) 

for _ in range(N):
    expressao = input()
    pilha = Stack()
    tem_duplicata = False
    
    for p in expressao:
        if p == ')':
            if pilha.peek() == '(':
                tem_duplicata = True
                break
            else:
                while not pilha.isEmpty() and pilha.peek() != '(':
                    pilha.pop()
                pilha.pop()
        else:
            pilha.push(p)
    
    if tem_duplicata:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicatas.')
            
            
        
        

        





        
        

            
            
        
        

        





        
        
