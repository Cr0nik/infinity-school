import random
import funcao_desafio1

print("""
    [1]: Pedra
    [2]: Papel
    [3]: Tesoura
""")

escolhas = [1, 2, 3]

escolha_jogador = int(input("Digite a sua escolha:"))
escolha_maquina = random.choice(escolhas)

funcao_desafio1.ganhador(escolha_jogador, escolha_maquina)


