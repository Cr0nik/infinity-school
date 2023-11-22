from modelos.crud import CRUD

banco = CRUD(
    database = 'teste.db',
    usuario = 'admin',
    senha = 'admin'
)

banco.inserir(
    table = 'usuarios',
    column = ('nome', 'idade'),
    values = ("Cesar", 24)
)