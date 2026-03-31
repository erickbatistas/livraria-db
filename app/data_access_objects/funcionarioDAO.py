from app.data_access_objects.baseDAO import BaseDAO

class FuncionarioDAO(BaseDAO):
    def inserir(self, funcionario):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO funcionario (nome, cargo, email) VALUES (%s, %s, %s)", 
                       (funcionario.nome, funcionario.cargo, funcionario.email))
        con.commit()
        cursor.close()
        con.close()

    def alterar(self, funcionario):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE funcionario SET nome=%s, cargo=%s, email=%s, ativo=%s WHERE id=%s", 
                       (funcionario.nome, funcionario.cargo, funcionario.email, funcionario.ativo, funcionario.id))
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE funcionario SET ativo=False WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, cargo, email FROM funcionario WHERE ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, cargo, email FROM funcionario WHERE id=%s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
