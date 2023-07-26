condicao = None
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

while condicao != False:
    acao = int(input('''Qual ação você deseja fazer? Lembrando que: 
     [1]: somar 
     [2]: multiplicar 
     [3]: maior 
     [4]: novos números 
     [5]: sair do programa'''))
    if acao == 1:
        soma = n1 + n2
        print(f'A soma entre o número {n1} + {n2} = {soma}')
    elif acao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} * {n2} = {multiplicacao}')
    elif acao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior do que o número {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que o número {n1}.')
        else:
            print('Não existe maior ou menor, os dois números são iguais.')
    elif acao == 4:
        n1 = int(input('Digite um número diferente do primeiro:'))
        n2 = int(input('Digite um número diferente do segundo:'))
    elif acao == 5:
        print('Você escolheu sair do programa.')
        condicao = False