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
    def __init__(self, titulo, autor, preco, estoque, id=None, ativo=True, categoria=None, fabricado_em_mari=False):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo
        self.categoria = categoria
        self.fabricado_em_mari = fabricado_em_mari


class Pedido:
    def __init__(self, id, cliente_id, data, estado, valor, pago, funcionario_id=None, forma_pagamento=None, desconto=0.0, status_confirmacao_pagamento="PENDENTE"):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
        self.estado = estado
        self.valor = valor
        self.pago = pago
        self.funcionario_id = funcionario_id
        self.forma_pagamento = forma_pagamento
        self.desconto = desconto
        self.status_confirmacao_pagamento = status_confirmacao_pagamento
        self.ativo = True


class PedidoItem:
    def __init__(self, pedido_id, livro_id, quantidade, id=None):
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
