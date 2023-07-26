from funcoes import verifica_A
palavra = input('Digite a palavra:')
if verifica_A(palavra) == True:
    print('A de amor.')
else:
    print(f'{palavra} não é A de amor.')