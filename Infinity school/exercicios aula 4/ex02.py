respondido = "S"
while respondido == "S":
    resposta = input('Deseja continuar?[S/N]').upper()
    respondido = resposta
    if respondido != "S" or respondido != "N":
        print("Entrada inválida.")
print("Fim!")