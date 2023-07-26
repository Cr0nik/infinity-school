def primo(numero):
    if numero <=1 :
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == False or numero % 3 == False:
        return False
    c = 5
    while c * c <= numero:
        if numero % c == False or numero(c + 2) == False:
            return False
        c +=6 
        return True
numero = int(input('Digite o número:'))
if primo(numero):
        divisao = 2
        print(f'O número {numero} é primo e é divisivel {divisao} vezes.')


