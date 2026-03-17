from data_access_objects.baseDAO import BaseDAO


class LivroDAO(BaseDAO):
    def inserir(self, livro):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO livro (titulo, autor, preco, estoque) VALUES (%s, %s, %s, %s)", 
                       (livro.titulo, livro.autor, livro.preco, livro.estoque))
        con.commit()
        cursor.close()
        con.close()

    def alterar(self, livro):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE livro SET titulo=%s, autor=%s, preco=%s, estoque=%s, ativo=%s WHERE id=%s", 
                       (livro.titulo, livro.autor, livro.preco, livro.estoque, livro.ativo, livro.id))
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
        cursor.execute("SELECT id, titulo, autor, preco, estoque FROM livro WHERE ativo=True")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque FROM livro WHERE id=%s", (id,)) # Hack, FIX: usar WHERE ativo=True para busca, cuidado pois quebra a lógica de remover()
        resultado = cursor.fetchone()
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

    def atualizar_quantidade(self, delta):
        pass
