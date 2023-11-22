import sqlite3 as sql

class CRUD:
    
    def __init__(self, database:str, usuario:str, senha:str):
        self.database = database
        self.usuario = usuario
        self.senha = senha
        
        self.conexao = None
        self.cursor = None
        
    #Métodos de conexão
    def logar(self):
        USUARIO = 'admin'
        SENHA = 'admin'
        
        return True if self.usuario == USUARIO and self.senha == SENHA else False
    
    
    def conectar(self):
        if self.logar() == True: #Login bem-sucedido
            self.conexao = sql.connect(self.database)
            self.cursor = self.conexao.cursor()
            return True
    
    
    def desconectar(self):
        if self.conectar() == True: #Se estiver conectado
            self.conexao.close()
            
            
    #Metodos do CRUD generico
    
    def inserir(self, table:str, column:tuple[str], values:tuple[any]): #Create
        
        '''
        Descrição:
        ------
        Esse metodo adiciona dados a coluna de alguma tabela
        
        Parametros: 
        ------
        tabela(str): Nome da tabela que será manipulada
        coluna(tupla[str]): coluna da tabela
        valores(tupla[any]): valores que serão inseridos na tabela
        
        '''
        
        if self.conectar() == True: #Se estiver conectado
            self.cursor.execute(
                f"INSERT INTO {table} {column} VALUES {values}"
            )
            self.conexao.commit()
            self.desconectar()
    
    
    def consultar(self, table:str, id:str): #Read
        if self.conectar == True: #Se estiver conectado
            dados = self.cursor.execute(
                f"SELECT * FROM {table} WHERE id = {id}"
            ).fetchall()
            self.desconectar()
            return dados
    
    
    def alterar(self): #Update
        if self.conectar == True: #Se estiver conectado
            pass
    
    
    def apagar(self): #Delete
        if self.conectar == True: #Se estiver conectado
            pass
    
    


if __name__ == "__main__": #Se o nome doo arquivo é igual a ele mesmo
    pass