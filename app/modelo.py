
from enum import Enum

class Livro:
    def __init__(self, id, titulo, autor, preco, estoque, ativo):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

class Cliente:
    def __init__(self, id, nome, numero, ativo):
        self.id = id
        self.nome = nome
        self.numero = numero
        self.ativo = ativo

class pedido:
    def __init__(self, id, cliente_id, data,Estado, valor, livro_id):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
        self.Estado = Estado
        self.livro_id = livro_id
        self.valor = valor
        self.pago = False
    
class EstadoPedido(str, Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"

class PedidoItem:
    def __init__(self, id, pedido_id, livro_id, quantidade):
        self.id = id
        self.pedido_id = pedido_id
        self.livro_id = livro_id
        self.quantidade = quantidade
