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
        
    def atualizar_dados(self, table_name, column_name, *values):
        self.conectar()
        self.cursor.execute(f"""UPDATE {table_name} SET {column_name} VALUES {values}
                            """)
        self.conexao.commit()
        
    def excluir_dados(self, table_name, column_name, *values):
        self.conectar()
        self.cursor.execute(f"""DELETE FROM {table_name} {column_name}VALUES {values}
                            """)
        self.conexao.commit()
        
    def cadastro(self, *values):
        self.conectar()
        self.cursor.execute("""
            INSERT INTO clientes (nome, email, cidade, estado, telefone, saldo) 
            VALUES (?, ?, ?, ?, ?, ?);
            """, values)
        self.conexao.commit()
        
    def cadastro_multiplo(self, usuarios):
        self.conectar()
        usuarios_validos = [usuario for usuario in usuarios if len(usuario) == 6]
        self.cursor.executemany("""
            INSERT INTO clientes (nome, email, cidade, estado, telefone, saldo) 
            VALUES (?, ?, ?, ?, ?, ?);
        """, usuarios_validos)
        self.conexao.commit()
