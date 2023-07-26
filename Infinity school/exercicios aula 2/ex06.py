salario = float(input('Digite o seu salario:'))
if salario <= 1320.00:
    salario = (0.15 * salario) + salario
    round(salario, 2)
    print(f'O valor do seu salario com aumento é de {salario}')
else:
    salario = (0.10 * salario) + salario
    round(salario, 2)
    print(f'O valor do seu salario com aumento é de {salario}')