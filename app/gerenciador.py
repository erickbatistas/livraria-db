from database import conectar

class BaseDAO   :
    """Classe pai para compartilhar a lógica de conexão"""
    def __init__(self):
        self.obter_conexao = conectar # Importado do seu database.py

class LivroDAO(BaseDAO):
    def inserir(self, livro):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("INSERT INTO livro (titulo, autor, preco, estoque) VALUES (%s, %s, %s, %s)", 
                       (livro.titulo, livro.autor, livro.preco, livro.estoque))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def alterar(self, livro):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE livro SET titulo=%s, autor=%s, preco=%s, estoque=%s, ativo=%s WHERE id=%s", 
                       (livro.titulo, livro.autor, livro.preco, livro.estoque, livro.ativo, livro.id))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def listar_todos(self):
        # Aqui você faria o SELECT * FROM livros
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque FROM livro")
        resultado = cursor.fetchall()
        print("Id   Título      Autor       Preço   Estoque")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}   {resultado[i][4]}")
        cursor.close()
        con.close()

    def gerar_relatorio(self):
        # Requisito 6: Exibir quantidade de elementos e valor total 
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*), SUM(preco * estoque) FROM livro")
        resultado = cursor.fetchone()
        print(f"Total de livros: {resultado[0]}")
        print(f"Valor total em estoque: R$ {resultado[1]}")
        cursor.close()
        con.close()

    def buscar_id(self, id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque FROM livro WHERE id=%s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado
    
    def remover(self, id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE livro SET ativo=False WHERE id=%s", (id,))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

class ClienteDAO(BaseDAO):
    def inserir(self, cliente):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("INSERT INTO cliente (nome, numero) VALUES (%s, %s)", 
                       (cliente.nome, cliente.numero))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def exibir_por_id(self, id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, numero FROM cliente WHERE id=%s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado #retorna none se não encontrar o cliente
    
    def alterar(self, cliente): #cliente é um objeto do tipo Cliente que tem os dados atualizados
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE cliente SET nome=%s, numero=%s, ativo=%s WHERE id=%s", 
                       (cliente.nome, cliente.numero, cliente.ativo, cliente.id))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def remover(self, id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE cliente SET ativo=False WHERE id=%s", (id,))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, numero FROM cliente")
        resultado = cursor.fetchall()
        print("Id   Nome       Número")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}")
        cursor.close()
        con.close()

    def buscar_por_nome(self, nome):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, numero FROM cliente WHERE nome ILIKE %s", (f"%{nome}%",))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado #retorna uma lista de clientes que tem o nome parecido com o buscado
    
    def gerar_relatorio(self):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM cliente")
        resultado = cursor.fetchone()
        print(f"Total de clientes: {resultado[0]}")
        cursor.close()
        con.close()

class PedidoDAO(BaseDAO):

    def inserir(self, pedido):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("INSERT INTO pedido (cliente_id, data, estado, valor, livro_id) VALUES (%s, %s, %s, %s, %s)", 
                       (pedido.cliente_id, pedido.data, pedido.Estado, pedido.valor, pedido.livro_id))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def alterar(self, pedido):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET cliente_id=%s, data=%s, estado=%s, valor=%s, livro_id=%s WHERE id=%s", 
                       (pedido.cliente_id, pedido.data, pedido.Estado, pedido.valor, pedido.livro_id, pedido.id))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def marcar_pago(self, id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET pago=True WHERE id=%s", (id,))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def exibir_por_id(self, id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data, estado, valor, livro_id FROM pedido WHERE id=%s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado #retorna none se não encontrar o pedido

    def atualizar_estado(self, id, novo_estado):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("UPDATE pedido SET estado=%s WHERE id=%s", (novo_estado, id))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def listar_todos(self):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data, estado, valor, livro_id FROM pedido")
        resultado = cursor.fetchall()
        print("Id   Cliente_Id   Data       Estado      Valor   Livro_Id")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}       {resultado[i][4]}   {resultado[i][5]}")
        cursor.close()
        con.close()

    def listar_por_cliente(self, cliente_id):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, cliente_id, data, estado, valor, livro_id FROM pedido WHERE cliente_id=%s", (cliente_id,))
        resultado = cursor.fetchall()
        print("Id   Cliente_Id   Data       Estado      Valor   Livro_Id")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}       {resultado[i][4]}   {resultado[i][5]}")
        cursor.close()
        con.close()

    def gerar_relatorio(self):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*), SUM(valor) FROM pedido")
        resultado = cursor.fetchone()
        print(f"Total de pedidos: {resultado[0]}")
        print(f"Valor total dos pedidos: R$ {resultado[1]}")
        cursor.close()
        con.close()

class PedidoItemDAO(BaseDAO):

    def inserir(self, pedido_item):
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES (%s, %s, %s)", 
                       (pedido_item.pedido_id, pedido_item.livro_id, pedido_item.quantidade))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def listar_por_pedido(self, pedido_id):

        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, pedido_id, livro_id, quantidade FROM pedido_item WHERE pedido_id=%s", (pedido_id,))
        resultado = cursor.fetchall()
        print("Id   Pedido_Id   Livro_Id   Quantidade")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}")
        cursor.close()
        con.close()

    def remover(self, id):
        
        con = self.obter_conexao()
        cursor = con.cursor()
        cursor.execute("DELETE FROM pedido_item WHERE id=%s", (id,))
        con.commit() # Salva no banco
        cursor.close()
        con.close()
