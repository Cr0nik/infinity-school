soma = 0
for i in range(6):
    numeros = int(input('Digite os números:'))
    if numeros % 2 == False:
        i += 1
        print(f'A quantidade de números pares é igual a {i}')
        soma += numeros
        print(f'A soma dos números pares é igual a {soma}')
    else:
        print('Esse número esta sendo desconsiderado, pois é impar.')
