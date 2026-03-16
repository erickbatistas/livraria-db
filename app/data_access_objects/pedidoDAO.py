from data_access_objects.baseDAO import BaseDAO


class PedidoDAO(BaseDAO):
    def inserir(self, pedido):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO pedido (cliente_id, data, estado, valor, livro_id) VALUES (%s, %s, %s, %s, %s)", 
                       (pedido.cliente_id, pedido.data, pedido.Estado, pedido.valor, pedido.livro_id))
        con.commit()
        cursor.close()
        con.close()

    def alterar(self, pedido):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET cliente_id=%s, data=%s, estado=%s, valor=%s, livro_id=%s WHERE id=%s", 
                       (pedido.cliente_id, pedido.data, pedido.Estado, pedido.valor, pedido.livro_id, pedido.id))
        con.commit()
        cursor.close()
        con.close()

    def remover(self):
        pass

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data, estado, valor, livro_id FROM pedido")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
        
    def listar_cliente(self, cliente_id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data, estado, valor, livro_id FROM pedido WHERE cliente_id=%s", (cliente_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data, estado, valor, livro_id FROM pedido WHERE id=%s", (id,))
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
        cursor.execute("SELECT COUNT(*), SUM(valor) FROM pedido")
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
    