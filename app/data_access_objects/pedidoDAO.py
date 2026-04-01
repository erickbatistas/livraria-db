try:
    from app.data_access_objects.baseDAO import BaseDAO
except ImportError:
    from data_access_objects.baseDAO import BaseDAO
from datetime import datetime


class PedidoDAO(BaseDAO):
    def inserir(self, pedido):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO pedido (cliente_id, funcionario_id, data_pedido, estado, valor, pago, forma_pagamento, desconto, status_confirmacao_pagamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                pedido.cliente_id,
                pedido.funcionario_id,
                datetime.now(),
                pedido.estado,
                pedido.valor,
                pedido.pago,
                pedido.forma_pagamento,
                pedido.desconto,
                pedido.status_confirmacao_pagamento,
            ),
        )
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        if con is None:
            raise Exception("Não foi possível conectar ao banco para remover pedido")
        cursor = con.cursor()
        cursor.execute("DELETE FROM pedido WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data_pedido, estado, valor, pago, forma_pagamento, status_confirmacao_pagamento FROM pedido WHERE ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
        
    def listar_cliente(self, cliente_id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data_pedido, estado, valor, pago, forma_pagamento, status_confirmacao_pagamento FROM pedido WHERE cliente_id=%s AND ativo=True ORDER BY id", (cliente_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data_pedido, estado, valor, pago, forma_pagamento, status_confirmacao_pagamento FROM pedido WHERE id=%s AND ativo=True ORDER BY id", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado # Retorna None se não encontrar o pedido

    def pagar(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET pago=True, status_confirmacao_pagamento='CONFIRMADO' WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def atualizar_estado(self, id, novo_estado):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET estado=%s WHERE id=%s", (novo_estado, id))
        con.commit()
        cursor.close()
        con.close()

    def atualizar_valor(self, pedido_id):
        con = self.conectar()
        if con is None:
            print("Não foi possível conectar ao banco para atualizar o valor do pedido.")
            return
            
        cursor = con.cursor()
        # Primeiro, calcula o valor bruto somando o preço dos livros nos itens do pedido
        # Se não houver itens, o valor do pedido é zerado.
        cursor.execute("""
            UPDATE pedido p
            SET valor = COALESCE((
                SELECT SUM(l.preco * pi.quantidade)
                FROM pedido_item pi
                JOIN livro l ON pi.livro_id = l.id
                WHERE pi.pedido_id = %s
            ), 0) * (1 - p.desconto)
            WHERE p.id = %s;
        """, (pedido_id, pedido_id))
        con.commit()
        cursor.close()
        con.close()

    def gerar_relatorio(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*), SUM(valor) FROM pedido WHERE ativo=True")
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
    
    def id_ultimo_pedido(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id FROM pedido WHERE ativo=True ORDER BY id DESC LIMIT 1")
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado[0] if resultado is not None else None