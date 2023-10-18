class Ingressos:
    def __init__(self, tipo:str, preco:float) -> None:
        self.preco = preco
        self.tipo = tipo
        self.__id = 0
        
    @property
    def identificador(self):
        return self.__id
    
    def idmodifier(self, valor:int):
        self.__id += valor
        
print('Iniciando cadastro...')
print('Preços: PISTA = 59,90 , CAMAROTE = 129,90 , VIP = 199,90')
print('Qual o tipo de ingresso você deseja comprar?')
tipo = input().lower()
if tipo == 'pista':
    preco = 59,90
elif tipo == 'camarote':
    preco = 129,90
elif tipo == 'vip':
    preco = 199,90
ingresso = Ingressos(tipo, preco)
ingresso.idmodifier(1)
print(vars(ingresso))
    
    