loop = True
while loop == True:
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
    escolha = int(input('Digite o número a sua escolha:'))
    if escolha > 10 and escolha < 0:
        print('ERRO! DIGITE UM NÚMERO VÁLIDO!')
    else:
        print(numeros[escolha])
    continuar = input('Deseja continuar? (S/N):').upper()
    if continuar == 'S':
        loop = True
    elif continuar == 'N':
        print('Obrigado por testar o programa :)')
        loop = False
    else:
        print('Digite uma saída válida. (S/N)')
    