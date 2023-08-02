frutas = ['limao', 'laranja', 'maracuja', 'abaicaxi', 'mexerica']
loop = True
while loop == True:
    fruta_desejada = input('Digite a fruta desejada:')
    if fruta_desejada in frutas:
        print(f'{fruta_desejada} adicionado a sacola.')
        resposta = input('Deseja adicionar algum item a mais na sacola?(S/N):').upper()
        if resposta == 'S':
            loop = True
        elif resposta == 'N':
            print('Fechando o seu pedido...')
            loop = False
        else:
            print('Digite uma resposta válida.')
    else:
        print('Essa fruta não está no nosso catálogo, digite novamente...')