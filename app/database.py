import psycopg2
from psycopg2 import OperationalError

def conectar():
    """Cria e retorna uma conexão com o banco de dados PostgreSQL."""
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="livraria_testes",
            user="postgres",
            password="senha",
            port="5432"
        )
        return conexao
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None