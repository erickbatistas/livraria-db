from data_access_objects.baseDAO import BaseDAO


class PedidoItemDAO(BaseDAO):
    def inserir(self, pedido_item):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT estoque, preco FROM livro WHERE id=%s", (pedido_item.livro_id,))
        valores_livro = cursor.fetchone()
        if valores_livro is None:
            print("\nLivro não encontrado.")
            sucesso = False
        else:
            if valores_livro[0] < pedido_item.quantidade:
                print("\nEstoque insuficiente.")
                sucesso = False
            else:
                cursor.execute("INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES (%s, %s, %s)", 
                            (pedido_item.pedido_id, pedido_item.livro_id, pedido_item.quantidade))
                cursor.execute("UPDATE livro SET estoque=estoque-%s WHERE id=%s", (pedido_item.quantidade, pedido_item.livro_id))
                cursor.execute("UPDATE pedido SET valor=valor+%s WHERE id=%s", (pedido_item.quantidade*valores_livro[1], pedido_item.pedido_id,))
                con.commit()
                sucesso = True
        cursor.close()
        con.close()
        return sucesso

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT p.quantidade, l.preco, p.pedido_id FROM pedido_item p INNER JOIN livro l ON p.livro_id = l.id WHERE livro_id=%s", (id,))
        valores = cursor.fetchone()
        cursor.execute("UPDATE livro SET estoque=estoque+%s WHERE id=%s", (valores[0], id))
        cursor.execute("UPDATE pedido SET valor=valor-%s WHERE id=%s", (valores[0]*valores[1], valores[2]))
        cursor.execute("DELETE FROM pedido_item WHERE livro_id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_pedido(self, pedido_id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT p.id, p.pedido_id, l.id, l.titulo, l.autor, l.preco, p.quantidade FROM pedido_item p INNER JOIN livro l ON p.livro_id=l.id WHERE pedido_id=%s", (pedido_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
