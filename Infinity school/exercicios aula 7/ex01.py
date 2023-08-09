valores = []
for i in range(1, 5):
    numeros = int(input(f'Digite {i}° número:'))
    valores.append(numeros)
if 2 in valores:
    print(f'Nessa lista o número 2 aparece: {valores.count(2)} veze(s).')
else:
    print('Nessa lista o número 2 não aparece.')
if 3 in valores:
    print(f'O primeiro número 3 da lista está na posição {valores.index(3) + 1}.')
else:
    print('Nessa lista não existe o valor 3.')
d4 = []
for valor in valores:
    if valor % 4 == 0:
        d4.append(valor)
        d4.sort()
rcolchete = str(d4)[1:-1] 
print(f'Os números multiplos de 4 em ordem crescente na lista são: {rcolchete}.')