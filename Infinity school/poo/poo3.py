class Veiculos:
    def __init__(self, nome:str, motores:int, rodas:bool) -> None:
        self.nome = nome
        self.motores = motores
        self.rodas = rodas
        
    def buzinar(self):
        pass
    
class Carro(Veiculos):
    def __init__(self, nome: str, motores: int, rodas: bool) -> None:
        super().__init__(nome, motores, rodas)
    
    def buzinar(self):
        return "Bi Bi"
    
class Barco(Veiculos):
    def __init__(self, nome: str, motores: int, rodas: bool) -> None:
        super().__init__(nome, motores, rodas)
        
    def buzinar(self):
        return "FOOOOOOOOOOOOOM"
    
class Aviao(Veiculos):
    def __init__(self, nome: str, motores: int, rodas: bool) -> None:
        super().__init__(nome, motores, rodas)
        
    def buzinar(self):
        return "IUIUIUIUIU"
    
veiculo = input("Digite o tipo do veiculo:").lower()
if veiculo == 'carro':
    nome = input('Digite o nome do veiculo:')
    motores = int(input('Digite a quantidade de motores do veiculo:'))
    rodas = input('O veiculo tem rodas?')
    if rodas == 's':
        rodas = True
    else:
        rodas = False
    veiculo = Carro(nome, motores, rodas)
    print(vars(veiculo))
    print(veiculo.buzinar())
elif veiculo == 'barco':
    nome = input('Digite o nome do veiculo:')
    motores = int(input('Digite a quantidade de motores do veiculo:'))
    rodas = input('O veiculo tem rodas?').lower()
    if rodas == 's':
        rodas = True
    else:
        rodas = False
    veiculo = Barco(nome, motores, rodas)
    print(vars(veiculo))
    print(veiculo.buzinar())
elif veiculo == 'aviao':
    nome = input('Digite o nome do veiculo:')
    motores = int(input('Digite a quantidade de motores do veiculo:'))
    rodas = input('O veiculo tem rodas?').lower()
    if rodas == 's':
        rodas = True
    else:
        rodas = False
    veiculo = Aviao(nome, motores, rodas)
    print(vars(veiculo))
    print(veiculo.buzinar())