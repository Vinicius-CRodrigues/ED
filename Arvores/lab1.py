class No:

     def __init__(self,d):

         self.dado = d

         self.esq = None

         self.dir = None



class ABB:

     def __init__(self,d):

        self.raiz = No(d)

     

     def insere(self, d):

         def insereRec(atual,no):

             if no.dado < atual.dado:

                 if atual.esq == None:

                    atual.esq = no

                 else:

                    insereRec(atual.esq,no)

             elif no.dado > atual.dado:

                  if atual.dir == None:

                    atual.dir = no

                  else:

                    insereRec(atual.dir,no)

         novo = No(d)

         if self.raiz == None:

            self.raiz = novo

         else:

            insereRec(self.raiz,novo)


def altura(ab):

    if ab is None:
        return 0
    
    def abrec(no):
        if no is None:
            return 0
        
        return 1 + max(abrec(no.esq), abrec(no.dir))
    
    return abrec(ab.raiz)

ab = ABB(1)
ab.insere(2)
ab.insere(3)
ab.insere(4)
print(altura(ab))