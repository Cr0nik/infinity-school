def pares(lista:list):
    for numero in lista:
        if numero % 2 != 0:
            lista.remove(numero)
    return lista

lista_teste = [1, 2, 3, 4, 5, 6]
print(pares(lista_teste))