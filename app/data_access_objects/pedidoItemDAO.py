try:
    from app.data_access_objects.baseDAO import BaseDAO
except ImportError:
    from data_access_objects.baseDAO import BaseDAO


class PedidoItemDAO(BaseDAO):
    def inserir(self, pedido_item):
        con = self.conectar()
        if con is None:
            raise Exception("Não foi possível conectar ao banco para inserir item de pedido")
        cursor = None
        try:
            cursor = con.cursor()
            cursor.execute("SELECT estoque, preco FROM livro WHERE id=%s FOR UPDATE", (pedido_item.livro_id,))
            valores_livro = cursor.fetchone()
            if valores_livro is None:
                print("\nLivro não encontrado.")
                sucesso = False
            else:
                if valores_livro[0] < pedido_item.quantidade:
                    print("\nEstoque insuficiente.")
                    sucesso = False
                else:
                    cursor.execute(
                        "SELECT id FROM pedido_item WHERE pedido_id=%s AND livro_id=%s FOR UPDATE",
                        (pedido_item.pedido_id, pedido_item.livro_id),
                    )
                    item_existente = cursor.fetchone()

                    if item_existente is None:
                        cursor.execute("INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES (%s, %s, %s)", 
                                       (pedido_item.pedido_id, pedido_item.livro_id, pedido_item.quantidade))
                    else:
                        cursor.execute(
                            "UPDATE pedido_item SET quantidade = quantidade + %s WHERE pedido_id=%s AND livro_id=%s",
                            (pedido_item.quantidade, pedido_item.pedido_id, pedido_item.livro_id),
                        )

                    cursor.execute("UPDATE livro SET estoque=estoque-%s WHERE id=%s", 
                                   (pedido_item.quantidade, pedido_item.livro_id))
                    cursor.execute("""
                        UPDATE pedido p
                        SET valor = COALESCE((
                            SELECT SUM(l.preco * pi.quantidade)
                            FROM pedido_item pi
                            JOIN livro l ON pi.livro_id = l.id
                            WHERE pi.pedido_id = p.id
                        ), 0) * (1 - p.desconto)
                        WHERE p.id = %s
                    """, (pedido_item.pedido_id,))
                    con.commit()
                    sucesso = True
        except Exception:
            if con:
                con.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            con.close()
        return sucesso

    def remover(self, pedido_id, livro_id):
        con = self.conectar()
        if con is None:
            raise Exception("Não foi possível conectar ao banco para remover item de pedido")
        cursor = None
        try:
            cursor = con.cursor()
            cursor.execute(("SELECT p.quantidade, l.preco FROM pedido_item p INNER JOIN livro l "
                            "ON p.livro_id = l.id WHERE p.pedido_id=%s AND p.livro_id=%s FOR UPDATE"), (pedido_id, livro_id),)
            valores = cursor.fetchone()
            if valores is not None:
                cursor.execute("UPDATE livro SET estoque=estoque+%s WHERE id=%s", (valores[0], livro_id))
                cursor.execute("DELETE FROM pedido_item WHERE pedido_id=%s AND livro_id=%s", (pedido_id, livro_id))
                cursor.execute("""
                    UPDATE pedido p
                    SET valor = COALESCE((
                        SELECT SUM(l.preco * pi.quantidade)
                        FROM pedido_item pi
                        JOIN livro l ON pi.livro_id = l.id
                        WHERE pi.pedido_id = p.id
                    ), 0) * (1 - p.desconto)
                    WHERE p.id = %s
                """, (pedido_id,))
                removido = True
            else:
                removido = False
            con.commit()
        except Exception:
            if con:
                con.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            con.close()
        return removido

    def listar_pedido(self, pedido_id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT p.id, p.pedido_id, l.id, l.titulo, l.autor, l.preco, p.quantidade FROM pedido_item p "
        "INNER JOIN livro l ON p.livro_id=l.id WHERE pedido_id=%s ORDER BY p.id", (pedido_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
