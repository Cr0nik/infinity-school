n = int(input('Digite o número:'))
cont =  n 
resp = str(n) + '!= ' + str(n)

print(f'Aqui esta o fatorial de {n}')
while cont > 1:
    cont -= 1
    resp += 'x' + str(cont)
    n *= cont

print(resp + '= ' + str(n))
    