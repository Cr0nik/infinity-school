numero_usuario = int(input('Digite um número:'))
soma = 0
for i in range(0, numero_usuario):
    if numero_usuario > 1000:
        print('Digite algum valor até 1000.')
        break
    soma = numero_usuario + i
    print(soma)
