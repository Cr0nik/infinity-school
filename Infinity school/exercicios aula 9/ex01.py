def soma_lista(lista:list) -> int:
    soma = sum(lista)
    return soma 

numeros = []
for i in range(0, 4):
    numero = int(input(f"Digite o {i + 1}° número:"))
    numeros.append(numero)
    
print(soma_lista(numeros))    