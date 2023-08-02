loop = True
while loop == True:
    nota = int(input('Digite uma nota até 10:'))
    if nota > 10:
        print('ERRO!, DIGITE NOVAMENTE.')
    else:
        print(f'A sua nota foi {nota}.')
        loop = False
    