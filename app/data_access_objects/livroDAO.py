try:
    from app.data_access_objects.baseDAO import BaseDAO
except ImportError:
    from data_access_objects.baseDAO import BaseDAO


class LivroDAO(BaseDAO):
    def inserir(self, livro):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO livro (titulo, autor, preco, estoque, categoria, fabricado_em_mari) VALUES (%s, %s, %s, %s, %s, %s)",
            (livro.titulo, livro.autor, livro.preco, livro.estoque, livro.categoria, livro.fabricado_em_mari),
        )
        con.commit()
        cursor.close()
        con.close()

    def alterar(self, livro):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute(
            "UPDATE livro SET titulo=%s, autor=%s, preco=%s, estoque=%s, ativo=%s, categoria=%s, fabricado_em_mari=%s WHERE id=%s",
            (livro.titulo, livro.autor, livro.preco, livro.estoque, livro.ativo, livro.categoria, livro.fabricado_em_mari, livro.id),
        )
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE livro SET ativo=False WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque, categoria, fabricado_em_mari FROM livro WHERE ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque, categoria, fabricado_em_mari FROM livro WHERE id=%s ORDER BY id", (id,)) # Hack, FIX: usar WHERE ativo=True para busca, cuidado pois quebra a lógica de remover()
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
    
    def buscar_por_nome(self, nome):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque, categoria, fabricado_em_mari FROM livro WHERE titulo ILIKE %s AND ativo=True ORDER BY id", (f'%{nome}%',))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_por_preco(self, preco_min, preco_max):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque, categoria, fabricado_em_mari FROM livro WHERE preco BETWEEN %s AND %s AND ativo=True ORDER BY preco", (preco_min, preco_max))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_por_categoria(self, categoria):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque, categoria, fabricado_em_mari FROM livro WHERE categoria ILIKE %s AND ativo=True ORDER BY id", (f'%{categoria}%',))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_fabricado_em_mari(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque, categoria, fabricado_em_mari FROM livro WHERE fabricado_em_mari=True AND ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
    
    def listar_pouco_estoque(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, estoque FROM vw_livros_pouco_estoque")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
    
    def gerar_relatorio(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*), SUM(preco * estoque) FROM livro")
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado

    def atualizar_quantidade(self, livro_id, delta):
        con = self.conectar()
        if con is None:
            raise Exception("Não foi possível conectar ao banco para atualizar quantidade do livro")
        cursor = con.cursor()
        cursor.execute("UPDATE livro SET estoque = estoque + %s WHERE id=%s RETURNING estoque", (delta, livro_id))
        resultado = cursor.fetchone()
        con.commit()
        cursor.close()
        con.close()
        return resultado[0] if resultado is not None else None
