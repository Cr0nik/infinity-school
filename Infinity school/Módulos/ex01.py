def nota(n1:float, n2:float):
    media = (n1 + n2)/2
    if media >= 6:
        aprovacao = print("APROVADO")
    else:
        aprovacao = print("REPROVADO")
    return media, aprovacao

nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))

nota(nota1, nota2)
