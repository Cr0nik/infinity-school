reta1 = int(input('Digite o valor da reta 1:'))
reta2 = int(input('Digite o valor da reta 2:'))
reta3 = int(input('Digite o valor da reta 3:'))

if reta1 == False and reta2 % 5 == False and reta3 % 3 == False:
    print('Isso pode se transformar em um triangulo.')
else:
    print('Isso não pode se transformar em um triangulo.')
