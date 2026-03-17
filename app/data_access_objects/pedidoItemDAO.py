from data_access_objects.baseDAO import BaseDAO


class PedidoItemDAO(BaseDAO):
    def inserir(self, pedido_item):
        con = self.conectar()
        cursor = con.cursor()
        # FIX: alterar o valor do pedido na tabela "pedido" ao inserir itens
        cursor.execute("INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES (%s, %s, %s)", 
                       (pedido_item.pedido_id, pedido_item.livro_id, pedido_item.quantidade))
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        # FIX: alterar o valor do pedido na tabela "pedido" ao remover itens
        cursor.execute("DELETE FROM pedido_item WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_pedido(self, pedido_id):
        con = self.conectar()
        cursor = con.cursor()
        # FIX: retornar titulo do livro ao inves de id
        cursor.execute("SELECT id, pedido_id, livro_id, quantidade FROM pedido_item WHERE pedido_id=%s", (pedido_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
