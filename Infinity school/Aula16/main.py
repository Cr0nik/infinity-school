from funcoes import Flashinha
from base_de_dados_de_clientes import BASE_DE_DADOS_CLIENTES


database = Flashinha("flashinha.db")

lista_dados = []

for x in BASE_DE_DADOS_CLIENTES:
    lista = []
    while len(lista) < 6:
        lista.append(x)
    else:
        lista_dados.append(lista)

for y in lista_dados:
    print(y)
