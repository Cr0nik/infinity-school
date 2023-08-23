def concatena(lista:list):
    s = ' '.join(lista) 
    s = s.replace(" !", "!")
    print(s)
    
lista_teste = ['Olá', 'mundo', '!']
concatena(lista_teste)