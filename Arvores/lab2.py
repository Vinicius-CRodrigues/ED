class No:

     def __init__(self,d):

         self.dado = d

         self.esq = None

         self.dir = None



class ABB:

     def __init__(self,noRaiz):

        self.raiz = noRaiz



     def imprimir(self):

         def imprimirRec(no,nivel,lado):

              if no:

                 print(lado,"-"*nivel,no.dado)

                 imprimirRec(no.esq,nivel+1,'E')

                 imprimirRec(no.dir,nivel+1, 'D')

         imprimirRec(self.raiz,0,'R')

def montaABBB(lista_ordenada):
    def construir_aux(inicio, fim):
        if inicio > fim:
            return None
        
        meio = (inicio + fim + 1) // 2
        
        raiz_subarvore = No(lista_ordenada[meio])
        raiz_subarvore.esq = construir_aux(inicio, meio - 1)
        raiz_subarvore.dir = construir_aux(meio + 1, fim)
        
        return raiz_subarvore

    if not lista_ordenada:
        return None
        
    return construir_aux(0, len(lista_ordenada) - 1)

	
raiz = montaABBB([1,2,3,4,5,6,7,90])
ab = ABB(raiz)
ab.imprimir()