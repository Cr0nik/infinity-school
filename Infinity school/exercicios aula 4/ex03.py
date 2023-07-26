nota1 = 0
while nota1 < 10:    
    nota = int(input("Digite a sua nota entre 0 e 10:"))
    if nota > 10:
        print("Digite uma nota até 10!")
    else:
        print(f"A sua nota foi {nota}")
        nota1 = 11
    