from data_access_objects.baseDAO import BaseDAO


class PedidoItemDAO(BaseDAO):
    def inserir(self, pedido_item):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES (%s, %s, %s)", 
                       (pedido_item.pedido_id, pedido_item.livro_id, pedido_item.quantidade))
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("DELETE FROM pedido_item WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_pedido(self, pedido_id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, pedido_id, livro_id, quantidade FROM pedido_item WHERE pedido_id=%s", (pedido_id,))
        resultado = cursor.fetchall()
        print("Id   Pedido_Id   Livro_Id   Quantidade")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}")
        cursor.close()
        con.close()
