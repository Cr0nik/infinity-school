import operacoes


n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))

sair = 'n'
while sair == 'n':

    escolha = str(input("Digite a operação desejada:")).lower()
    if escolha == 'soma':
        print(f"A soma dos valores escolhidos é de: {operacoes.soma(n1, n2)}")
        sair = input('Você deseja sair da calculadora? (S/N):').lower()
    elif escolha == 'subtracao':
        print(f"A subtração dos valores escolhidos é de: {operacoes.subtracao(n1, n2)}")
        sair = input('Você deseja sair da calculadora? (S/N):').lower()

    elif escolha == 'multiplicacao':
        print(f"A multiplicação dos números escolhidos é de: {operacoes.multiplicacao(n1, n2)}")
        sair = input('Você deseja sair da calculadora? (S/N):').lower()
        
    elif escolha == 'divisao':
        print(f"A divisão dos números escolhidos é de: {operacoes.divisao(n1, n2)}")
        sair = input('Você deseja sair da calculadora? (S/N):').lower()
        
    elif escolha == 'potencia':
        print(f"A poência dos números escolhidos é de: {operacoes.potencia(n1, n2)}")
        sair = input('Você deseja sair da calculadora? (S/N):').lower()
        