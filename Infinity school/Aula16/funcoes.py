import sqlite3 as sql


class Flashinha():
    
    def __init__(self, database) -> None:
        self.database = database
        self.conexao = None
        self.cursor = None
    
    def conectar(self):
        self.conexao = sql.connect(self.database)
        self.cursor = self.conexao.cursor()
         
    def criar_tabela(self, table_name, sql_query):
        self.conectar()
        self.cursor.execute(f"""
                            CREATE TABLE {table_name} ({sql_query})
                            """)
        self.conexao.commit()
        
    def adicionar_dados(self, table_name, column_name, *values):
        self.conectar()
        self.cursor.execute(f"""INSERT INTO {table_name} {column_name}VALUES {values}
                            """)
        self.conexao.commit()
        
        