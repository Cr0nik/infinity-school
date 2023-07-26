condicao = True
usuario = input('Digite o seu nome de usuário:')
senha = input('Digite a sua senha:')

while condicao == True:
    if usuario == senha:
        print('ERRO, crie uma nova senha:')
        senha = input('Digite uma nova senha:')
    else:
        print('A sua nova senha foi redefinida.')
        condicao = False