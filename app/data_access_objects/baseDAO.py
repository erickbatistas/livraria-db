from app.database import conectar


class BaseDAO:
    # Classe pai para compartilhar a lógica de conexão
    def __init__(self):
        self.conectar = conectar