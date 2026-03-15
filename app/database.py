import psycopg2
from psycopg2 import OperationalError

import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o sistema para nao expor senhas

load_dotenv()

def conectar():
    """Cria e retorna uma conexão com o banco de dados PostgreSQL."""
    try:
        conexao = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conexao
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None