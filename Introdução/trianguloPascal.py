def triangulo(n: int):
    pascal = []
    for i in range(n):
        linha = [1] * (i + 1)
        for j in range(1, i):
            linha[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(linha)
    return pascal

print(triangulo(5))

