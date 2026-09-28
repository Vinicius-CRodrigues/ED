def caminho(grafo, i, f, visitados=None):
    # Inicializa o conjunto de visitados na primeira chamada da função
    if visitados is None:
        visitados = set()

    ni = grafo.getVertex(i)
    nf = grafo.getVertex(f)
    
    # Se algum dos vértices não existir, retorna None
    if ni == None or nf == None:
        return None
    
    # Caso base: se o início já é o destino, o caminho é ele mesmo
    if i == f:
        return [i]
    
    # Marca o vértice atual como visitado para evitar ciclos nesta ramificação
    visitados.add(i)
        
    for v in ni.getConnections():
        v_id = v.getId()
        
        # Se o vizinho já foi visitado neste caminho, ignora para não entrar em ciclo
        if v_id in visitados:
            continue
            
        # Faz a chamada recursiva partindo do vizinho atual
        caminhoFinal = caminho(grafo, v_id, f, visitados)
        
        if caminhoFinal != None:
            caminhoFinal.insert(0, ni.getId()) 
            return caminhoFinal
            
    # Backtracking: remove o vértice atual dos visitados ao retornar 
    # para permitir que ele seja explorado por outros caminhos alternativos
    visitados.remove(i)
    return None                                                                                                                                                                                                                                                                 