class ContaBancaria:
    def __init__(self, numero:str, chave:str) -> None:
        self.numero = numero
        self.chave = chave 
        self.__saldo = 0
        
        
    @property
    def saldo(self):
        return self.__saldo
    
    
    @saldo.setter
    def saldo(self, novo_saldo):
        raise ValueError('Meu programa é seguro, você so altera o saldo se fizer por meio de um método.')
    
     
    def depositar(self, valor:float):
        self.__saldo += valor
    
    
conta1 = ContaBancaria('423879-1', 'rafinhamatador20comer@gmail.com')
conta1.depositar(1_000_000)

try:
    conta1.saldo = 4_000_000
except ValueError as e:
    print(e)
      
print(vars(conta1))