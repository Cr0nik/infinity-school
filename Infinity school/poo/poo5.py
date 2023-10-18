class Funcionario:
    def __init__(self, nome:str, dia_trabalhado:int, valor_dia:float) -> None:
        self.nome = nome
        self.dia_trabalhado = dia_trabalhado
        self.valor_dia = valor_dia
        self.__salario = 0
        
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def saldo(self, salario):
        raise ValueError('Para de tentar mudar o salário ai vagabundo, vai trabalhar.')
    
    def calculo_salario(self):
        self.__salario = self.valor_dia * self.dia_trabalhado
        
    
nome = input('Digite o seu nome:')
diasT = int(input('Dias trabalhados:'))
valorD = 102.46

funcionario = Funcionario(nome, diasT, valorD)
funcionario.calculo_salario()
print(funcionario.salario)