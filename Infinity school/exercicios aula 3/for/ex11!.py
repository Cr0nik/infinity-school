peso_lista = []
for i in range(5):
    peso = float(input('Digite o seu peso:'))
    peso_lista.append(peso)
maior = peso_lista[0]
menor = peso_lista[0]
for peso in peso_lista:
    if peso > maior:
        maior = peso
for peso in peso_lista:
    if peso < menor:
        menor = peso
print(f'O maior peso é de {maior}kg, e o menor é {menor}kg.')
