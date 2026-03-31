from app.data_access_objects.baseDAO import BaseDAO


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
        cursor.execute("UPDATE cliente SET ativo=False WHERE id=%s", (id,)) #SOFT DELETE: apenas marca o cliente como inativo, sem remover da base de dados
        con.commit()
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email FROM cliente WHERE ativo=True ORDER BY id")
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    def buscar_id(self, id): #busca uma linha por id
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email FROM cliente WHERE id=%s ORDER BY id", (id,)) # FIX: usar WHERE ativo=True para busca, quebra a lógica de remover()
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado # Retorna None se não encontrar o cliente

    def buscar_nome(self, nome):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, email FROM cliente WHERE nome ILIKE %s AND ativo=True ORDER BY id", (f"%{nome}%",))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado # Retorna uma lista de clientes que tem o nome parecido com o buscado
    
    def gerar_relatorio(self):
        con = self.conectar()
        cursor = con.cursor()
        query = """
            SELECT 
                c.id,
                c.nome, 
                c.email, 
                COUNT(p.id) AS total_pedidos, 
                COALESCE(SUM(p.valor), 0) AS total_gasto,
                MAX(p.data_pedido) AS data_ultima_compra,
                COALESCE(AVG(p.valor), 0) AS ticket_medio
            FROM cliente c
            LEFT JOIN pedido p ON c.id = p.cliente_id 
                 AND p.data_pedido >= NOW() - INTERVAL '6 months'
            WHERE c.ativo = True
            GROUP BY c.id, c.nome, c.email
            ORDER BY total_gasto DESC
        """
        cursor.execute(query)
        
        #RELATÓRIO: lista os clientes ativos e quantos pedidos eles fizeram nos últimos 6 meses, ordenado do cliente que mais comprou para o que menos comprou

        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
    