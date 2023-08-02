n1 = int(input('Digite os números:'))
n2 = int(input('Digite os números:'))
n3 = int(input('Digite os números:'))
n4 = int(input('Digite os números:'))
numeros = (n1, n2, n3, n4)
if 3 in numeros:
    primeiro3 = numeros.index(3) + 1
    print(f'O primeiro número 3 aparece na posição {primeiro3}')
numeros.count(2)
print(f'O número 2 apareceu {numeros.count(2)} veze(s).')
d4 = []
for numero in numeros:
    if numero % 4 == 0:
        d4.append(numero)
print(f'{d4}, são divisíveis por 4.')