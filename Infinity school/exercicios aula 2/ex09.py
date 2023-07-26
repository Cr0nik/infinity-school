from funcoes import verificar_ponto
n = input('Digite o número:')
#checar se é decimal ou inteiro  
if verificar_ponto(n) == True:
    n = float(n)
    print('O número é decimal.')
else:
    n = int(n)
    print('O número é inteiro.')
#checar se é par ou impar
if n % 2 == False:
    print('O número é par.')
else:
    print('O número é ímpar.')
#checar se é positivo ou negativo
if n >= 0:
    print('O número é positivo.')
else:
    print('O número é negativo.')