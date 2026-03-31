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
    def __init__(self, id, cliente_id, data, estado, valor, pago, funcionario_id=None, forma_pagamento=None, desconto=0.0):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
        self.estado = estado
        self.valor = valor
        self.pago = pago
        self.funcionario_id = funcionario_id
        self.forma_pagamento = forma_pagamento
        self.desconto = desconto
        self.ativo = True


class PedidoItem:
    def __init__(self, id, pedido_id, livro_id, quantidade):
        self.id = id
        self.pedido_id = pedido_id
        self.livro_id = livro_id
        self.quantidade = quantidade


class Funcionario:
    def __init__(self, id, nome, cargo, email, ativo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.email = email
        self.ativo = ativo


class Fornecedor:
    def __init__(self, id, nome, email, telefone, ativo):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.ativo = ativo
