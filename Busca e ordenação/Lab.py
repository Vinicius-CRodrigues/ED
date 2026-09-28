def quickSort(alist):
    if len(alist) <=1:
        return alist
    esquerda, pivo, direita = reordena(alist)
    esquerda = quickSort(esquerda)
    direita = quickSort(direita)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist):
    esquerda = []
    direita = []
    pivo = alist[-1]

    for i in alist[:-1]:
        if pivo <= i:
            esquerda.append()
        elif pivo >= i:
            direita.append()

    return esquerda, pivo, direita