numeros_pares = 0 
numeros_impares = 0
for i in range(10):
    numero = int(input('Digite os numeros:'))
    if numero % 2 == False:
        numeros_pares += 1
    else:
        numeros_impares += 1
print(f'A quantidade de números pares é igual a {numeros_pares}')
print(f'A quantidade de números impares é igual a {numeros_impares}')