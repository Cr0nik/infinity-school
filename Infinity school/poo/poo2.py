class Animal:
    def __init__(self, nome:str, raca: str, peso:float) -> None:
        self.nome = nome
        self.raca = raca
        self.peso = peso
    
    def emitir_som(self):
        print("Emitindo som.....")
        
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, peso: float) -> None:
        super().__init__(nome, raca, peso)
    
    def emitir_som(self):
        return "AU AU AU"
        
class Gato(Animal):
    def __init__(self, nome: str, raca: str, peso: float) -> None:
        super().__init__(nome, raca, peso)
        
    def emitir_som(self):
        return 'Miau Miau Miau'
        
def fazer_barulho(animal):
    return animal.emitir_som()
  
animal = input("Digite o seu animal:").lower()
nome = input("Digite o nome do seu animal:")
raca = input("Digite a raça do seu animal:")
peso = float(input("Digite o peso do seu animal:"))

if animal == 'cachorro':
    animal = Cachorro(nome, raca, peso)
    print(fazer_barulho(animal))
else:
    animal = Gato(nome, raca, peso)
    print(fazer_barulho(animal))