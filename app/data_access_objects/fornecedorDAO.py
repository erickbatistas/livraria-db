try:
    from app.data_access_objects.baseDAO import BaseDAO
except ImportError:
    from data_access_objects.baseDAO import BaseDAO

class FornecedorDAO(BaseDAO):
    def inserir(self, fornecedor):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO fornecedor (nome, email, telefone) VALUES (%s, %s, %s)", 
                       (fornecedor.nome, fornecedor.email, fornecedor.telefone))
        con.commit()
        cursor.close()
        con.close()

    def alterar(self, fornecedor):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE fornecedor SET nome=%s, email=%s, telefone=%s, ativo=%s WHERE id=%s", 
                       (fornecedor.nome, fornecedor.email, fornecedor.telefone, fornecedor.ativo, fornecedor.id))
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE fornecedor SET ativo=False WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM fornecedor WHERE ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM fornecedor WHERE id=%s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
