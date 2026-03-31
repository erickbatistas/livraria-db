from enum import Enum


class Cliente:
    def __init__(self, nome, id=None, email=None, ativo=True):
        self.id = id
        self.nome = nome
        self.email = email
        self.ativo = ativo


class EstadoPedido(str, Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"


class Livro:
    def __init__(self, titulo, autor, preco, estoque, id=None, ativo=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo


class Pedido:
    def __init__(self, cliente_id, id=None, data=None, estado="EM_ANDAMENTO", valor=0.0, pago=False):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
        self.estado = estado
        self.valor = valor
        self.pago = pago
        self.ativo = True


class PedidoItem:
    def __init__(self, pedido_id, livro_id, quantidade, id=None):
        self.id = id
        self.pedido_id = pedido_id
        self.livro_id = livro_id
        self.quantidade = quantidade
