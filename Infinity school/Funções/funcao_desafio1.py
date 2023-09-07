def ganhador(humano:int, maquina:int) -> int:
    if humano == maquina:
        print("EMPATE!")

    elif humano == 1 and maquina == 2:
        print("VOCÊ PERDEU!")

    elif humano == 2 and maquina == 1:
        print("VOCÊ GANHOU!")
    
    elif humano == 3 and maquina == 1:
        print("VOCÊ PERDEU!")
    
    elif humano == 1 and maquina == 3:
        print("VOCÊ GANHOU!")

    elif humano == 2 and maquina == 3:
        print("VOCÊ PERDEU!")

    elif humano == 3 and maquina == 2:
        print("VOCÊ GANHOU!")







