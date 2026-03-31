from data_access_objects.baseDAO import BaseDAO


class PedidoDAO(BaseDAO):
    def inserir(self, pedido):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO pedido (cliente_id, funcionario_id, estado, valor, pago, forma_pagamento, desconto) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (pedido.cliente_id, pedido.funcionario_id, pedido.estado, pedido.valor, pedido.pago, pedido.forma_pagamento, pedido.desconto))
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
        cursor.execute("SELECT id, cliente_id, data_pedido, estado, valor, pago FROM pedido WHERE ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
        
    def listar_cliente(self, cliente_id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data_pedido, estado, valor, pago FROM pedido WHERE cliente_id=%s AND ativo=True ORDER BY id", (cliente_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data_pedido, estado, valor, pago FROM pedido WHERE id=%s AND ativo=True ORDER BY id", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado # Retorna None se não encontrar o pedido

    def pagar(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET pago=True WHERE id=%s", (id,))
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