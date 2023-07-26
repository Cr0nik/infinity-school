vcasa = int(input('Digite o valor da casa:'))
vsalario = int(input('Digite o seu salário:'))
anos = int(input('Digite a quantidade de anos que quitará o emprestimo:'))

prestacoes = anos * 12
vcasa = vcasa / prestacoes

if vcasa <= vsalario * 0.30:
    print('O emprestimo foi aprovado!')
else: 
    print('O emprestimo foi negado!')
print(f'O valor de cada parcela seria de {vcasa}')
