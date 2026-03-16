from data_access_objects.baseDAO import BaseDAO


class ClienteDAO(BaseDAO):
    def inserir(self, cliente):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO cliente (nome, email) VALUES (%s, %s)", 
                       (cliente.nome, cliente.email))
        con.commit()
        cursor.close()
        con.close()

    def alterar(self, cliente): # cliente é um objeto do tipo Cliente que tem os dados atualizados
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE cliente SET nome=%s, email=%s, ativo=%s WHERE id=%s", 
                       (cliente.nome, cliente.email, cliente.ativo, cliente.id))
        con.commit()
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE cliente SET ativo=False WHERE id=%s", (id,))
        con.commit()
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email FROM cliente WHERE ativo=True")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email FROM cliente WHERE id=%s", (id,)) # FIX: usar WHERE ativo=True para busca, quebra a lógica de remover()
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado # Retorna None se não encontrar o cliente

    def buscar_nome(self, nome):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email FROM cliente WHERE nome ILIKE %s AND ativo=True", (f"%{nome}%",))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado # Retorna uma lista de clientes que tem o nome parecido com o buscado
    
    def gerar_relatorio(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM cliente")
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
    