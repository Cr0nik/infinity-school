from funcoes import Flashinha
from base_de_dados_de_clientes import BASE_DE_DADOS_CLIENTES

database = Flashinha("flashinha.db")

usuarios = []

# Construa a lista de usuários fora do loop
for i in range(0, len(BASE_DE_DADOS_CLIENTES), 6):
    usuario = BASE_DE_DADOS_CLIENTES[i:i + 6]
    usuarios.append(usuario)


database.cadastro_multiplo(usuarios)


#Criando a conta:
criar_conta = True
log = input("LogIn ou SignIn?(L/S)").lower()
if log == 's':
    criar_conta == False

while criar_conta == True:
    
    new_user = []
    
    nome = input("Digite o seu nome:")
    email = input("Digite o seu email:")
    cidade = input("Digite a sua cidade:")
    estado = input("Digite o seu estado:")
    telefone = input("Digite o seu telefone:")
    saldo = float(input("Digite o seu saldo:"))
    
    new_user.append(nome, email, cidade, estado, telefone, saldo)
    
    database.cadastro(new_user)
    
    print("Conta criada com sucesso!!")
    break
