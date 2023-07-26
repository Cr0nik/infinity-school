quantidade_maior = 0
quantidade_menor = 0
ano_atual = int(input('Digite o ano em que estamos:'))
for i in range(0, 7):
    ano = int(input('Digite o ano em que voce nasceu:'))
    maior_idade = ano_atual - ano
    if maior_idade >= 18:
        quantidade_maior += 1
    else:
        quantidade_menor += 1
print(f'{quantidade_maior} pessoas são maiores de idade.')
print(f'{quantidade_menor} pessoas são menores de idade.')

